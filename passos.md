1 - [] Subir IAC 

2 - [] aws eks update-kubeconfig --region us-east-1 --name btc-edc-m3-eks

3 - [] helm repo add apache-airflow https://airflow.apache.org

4 - [] kubectl create ns airflow

5 - [] kubectl create secret -n airflow generic aws-secret
--from-literal=AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>
--from-literal=AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>
--from-literal=AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION>

6 - [] kubectl apply -f manifests/airflow-crb.yaml -n airflow

7 - [] Criar a fernet key e webserver secret key do arquivo do airflow python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())" python -c 'import secrets; print(secrets.token_hex(16))'

8 - [] Criar bucket de logs do airflow, precisa colocar o caminho no manifesto do airflow linha 1688 remote_base_log_folder: s3://nome-do-seu-bucket/edc-btc-m3 remote_log_conn_id: my_s3_conn

9 - [] Colocar o caminho das dags no manifest do airflow 1787 repo: https://github.com/diegoriciardi/airflow-dags.git branch: main rev: HEAD depth: 1 subpath: "dags"

10 - [] Fazer / Conferir arquivos dags

11 - [] Subir dags no github

12 - helm repo add apache-airflow https://airflow.apache.org

13 - helm repo update

14 - [] helm install airflow apache-airflow/airflow --version 1.7.0 -n airflow -f manifests/airflow-values.yaml

15 - [] helm repo add spark-operator https://googlecloudplatform.github.io/spark-on-k8s-operator

16 - [] helm repo update

17 - [] helm install spark-operator spark-operator/spark-operator --namespace processing --create-namespace -f manifests/spark-operator-values.yaml --version 1.1.26

18 - [] kubectl create secret -n processing generic aws-secret
--from-literal=AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>
--from-literal=AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>
--from-literal=AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION>

19 - [] kubectl port-forward service/airflow-webserver -n airflow 8080:8080

20 - [] Cadastrar a connection em admin connections. "my_s3_conn" na UI do Airflow: connection type Amazon Web Services

21 - [] Criar cluster connection id no airflow kubernetes_default connection type Kubernetes Cluster Connection. Em admin > connections marcar a caixinha in cluster configuration

22 - [] Criar variavel de ambiente combustiveis_source_urls e enem_source_urls no airflow em admin > variables

[ "https://download.inep.gov.br/microdados/microdados_enem_2020.zip" ]

23 - [] Criação dos buckets para a camada landing e a camada bronze. Colocar os nomes dos buckets criados no arquivo aws da pasta docker>scripts>app>config>aws.py

24 - [] Conferir arquivos de ingestão e processamento do job

25 - [] Buildar e subir a imagem docker build -t diegoriciardi/desafio-btc-edc-final-m5-spark:9.9.9 -f docker/spark-operator.Dockerfile docker/ --no-cache

27 - [] docker push diegoriciardi/desafio-btc-edc-final-m5-spark:9.9.9

28 - [] Rodar o job no airflow