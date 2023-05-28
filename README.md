<h1 align="center">
  🚀 AIRFLOW DATA ENGINEERING 🚀
</h1>

<h2 align="center">
  📚 Engenharia de dados com Apache Airflow no Google Cloud 📚
</h2>

### 🎯 Projeto:
Este projeto aproveita a versatilidade do Google Composer e a potência do Apache Airflow para criar um orquestrador de dados robusto. Usamos uma imagem de Apache Airflow para implantar a orquestração de dados a partir de uma API até o Google Storage, onde são armazenados em formato JSON.

### 💻 Tecnologias utilizadas:
* [Apache Airflow](https://airflow.apache.org/) 🌪
* [Python](https://www.python.org/) 🐍
* [Google Cloud](https://cloud.google.com/) ☁
* [Docker](https://www.docker.com/) 🐳

### 🌐 Como implantar na Cloud:
1. Clone o repositório.
2. Crie uma conta no Google Cloud Platform (GCP).
3. Configure um usuário administrador no Identity and Access Management (IAM).
4. Crie um ambiente no Google Composer usando uma imagem do Apache Airflow.
5. Carregue os arquivos do pacote Dags que começam com "nytimes".
6. Crie um bucket no Google Storage.
7. Na dag, altere o nome do bucket para o que você criou. Por padrão, ele é chamado de "airflow-api-backups".
8. Volte para o Composer e acesse o painel do Airflow.
9. No painel, você verá a dag adicionada que você pode acionar.

### 💼 Como rodar localmente:
1. Clone o repositório.
2. Instale o Docker em sua máquina.
3. Abra o terminal e navegue até o diretório do repositório clonado.
4. Execute `docker-compose up -d --build` para construir a imagem e subi-la em um contêiner Docker. 
5. Quando os contêineres estiverem em execução, acesse `localhost:8080` em seu navegador. Você terá acesso ao painel do Airflow com as dags criadas.

### 👏 Créditos:
Este projeto é uma colaboração de:

**Djalma Henrique Silva Lima**  
Github: [DjalmaHenry](https://github.com/DjalmaHenry/)

**Ronny Lima Ribeiro da Silva**  
Github: [ronnylrsd](https://github.com/ronnylrsd)

Vamos juntos fazer a engenharia de dados mais acessível e eficiente para todos! 🎉🙌
