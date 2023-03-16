# DGA (Directed Acyclic Graphs):
# Tarefas ligadas por setas de forma acíclica, tem início e fim.
# Trabalha por baixo dos panos com grafos.
# composto por tasks, que realizam uma função (transformação).
# EX: inserção no banco de dados.

# Tasks:
# Tarefas em paralelo ou ter precendência.

# Importações usando Python:

from airflow import DAG
from datetime import datetime
# Operador que vai operar as tasks
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
import pandas as pd
import requests
import json

# DAG('id da dag', início da execução da dag, intervalo de tempo de execução do DAG [padrões usados da crontab do unix], a partir da data de ínicio todos os dags vai criar uma dag e executar [true, false])

# O início da dag é o start_date + schedule_interval


def handle_capture_count_data():
    url = "https://data.cityofnewyork.us/resource/rc75-m7u3.json"
    response = requests.get(url)
    df = pd.DataFrame(json.loads(response.content))
    qtd = len(df.index)
    return qtd

# xcom -> função do airflow, comunicate message (compartilhar informações entre tasks) usando o task_instance


def handle_is_suited(task_instance):
    qtd = task_instance.xcom_pull(task_ids='capture_count_data')
    if (qtd > 1000):
        return 'suited'
    return 'unsuited'


with DAG('tutorial_executa_dag', start_date=datetime(2021, 12, 1), schedule_interval='30 * * * *', catchup=False) as dag:
    capture_count_data = PythonOperator(
        task_id='capture_count_data',
        python_callable=handle_capture_count_data
    )

    is_suited = BranchPythonOperator(
        task_id='is_suited',
        python_callable=handle_is_suited
    )

    suited = BashOperator(
        task_id='suited',
        bash_command="echo 'Quantidade OK'"
    )
    unsuited = BashOperator(
        task_id='unsuited',
        bash_command="echo 'Quantidade não OK'"
    )

capture_count_data >> is_suited >> [suited, unsuited]

# botao pra executar e parar
# clear para limpar as tasks
