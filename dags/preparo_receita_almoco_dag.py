import json
from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator

# Caminho absoluto do a pasta onde este arquivo está localizado
caminho_absoluto = os.path.dirname(os.path.abspath(__file__))


def verificar_tempo_preparo(**kwargs):
    with open(os.path.join(caminho_absoluto, 'receita.json'), 'r') as f:
        dados_receita = json.load(f)
        receita_almoco = None
        for receita in dados_receita['receitas']:
            if receita['nome'] == 'Almoço':
                receita_almoco = receita
                break

    tempo_preparo = receita_almoco['time']
    agora = datetime.now()
    limite = agora.replace(hour=12, minute=0, second=0)

    tempo_restante = limite - agora
    segundos_restante = tempo_restante.total_seconds()

    if tempo_preparo <= segundos_restante:
        with open(os.path.join(caminho_absoluto, 'receita.txt'), 'a') as f:
            f.write('Há tempo suficiente para preparar a receita.\n')
        return True
    else:
        with open(os.path.join(caminho_absoluto, 'receita.txt'), 'a') as f:
            f.write('Não há tempo suficiente para preparar a receita.\n')
        raise ValueError('Não há tempo suficiente para preparar a receita.')


def formatar_receita(**kwargs):
    with open(os.path.join(caminho_absoluto, 'receita.json'), 'r') as f:
        dados_receita = json.load(f)
        receita_almoco = None
        for receita in dados_receita['receitas']:
            if receita['nome'] == 'Almoço':
                receita_almoco = receita
                break

    with open(os.path.join(caminho_absoluto, 'receita.txt'), 'a') as f:
        f.write('Receita: {}\n'.format(receita_almoco['nome']))
        f.write('Ingredientes:\n')
        for ingrediente in receita_almoco['ingredientes']:
            f.write(' - {}\n'.format(ingrediente))

        f.write('Instruções:\n')
        for i, instrucao in enumerate(receita_almoco['instrucoes']):
            f.write('{}. {}\n'.format(i + 1, instrucao))


def informar_fim(**kwargs):
    with open(os.path.join(caminho_absoluto, 'receita.txt'), 'a') as f:
        f.write('FIM\n')


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'start_date': datetime(2023, 4, 16),
}

dag = DAG(
    'preparo_receita_almoco',
    default_args=default_args,
    description='DAG que verifica o tempo de preparo da receita e formata o JSON em uma receita legível',
    schedule_interval=None,
    catchup=False
)

inicio = DummyOperator(task_id='inicio', dag=dag)

tarefa_verificar_tempo_preparo = PythonOperator(
    task_id='verificar_tempo_preparo',
    python_callable=verificar_tempo_preparo,
    provide_context=True,
    dag=dag
)

tarefa_formatar_receita = PythonOperator(
    task_id='formatar_receita',
    python_callable=formatar_receita,
    provide_context=True,
    dag=dag
)

tarefa_informar_fim = PythonOperator(
    task_id='informar_fim',
    python_callable=informar_fim,
    provide_context=True,
    dag=dag
)

fim = DummyOperator(task_id='fim', dag=dag)

inicio >> [tarefa_verificar_tempo_preparo,
           tarefa_formatar_receita] >> tarefa_informar_fim >> fim
