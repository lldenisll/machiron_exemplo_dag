# Machiron - Hello World de Airflow (exemplo Pokemon)

#### Crie uma virtualenv e instale os requirements

```bash
python -m venv airflow
source airflow/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

#### Inicie o banco de dados do airflow e o webserver
Lembre-se de que o Airflow irá rodar na porta 8080, garanta que ela esteja disponível, ou altere nas configurações do airflow a porta.
- Exporte a variavel de ambiente do path para o airflow
`export AIRFLOW_HOME="$(pwd)"`

- Inicie o db do airflow
	`airflow db init`


- Execute o webserver
`airflow webserver`

- Em outro terminal execute o scheduler (ative a virtualenv novamente)
`airflow scheduler`



### Acesso a interface Airflow

- Acesse [localhost:8080](http://localhost:8080 "localhost:8080") e verifique que se o Airflow está disponível. 
- Você será capaz de acessar a DAG "Exemplo" se tudo estiver corrido bem.  
- Veja mais detalhes de como usar o painel do airflow na[ nossa página do Notion](https://www.notion.so/Airflow-Denis-ad99dfdf87014f648892c1793eaf41b9#3b664074cdd643e1afcd8631df9b1615 " nossa página do Notion")


### Possíveis erros e configuações opcionais
- Caso a DAG exemplo não apareça, você pode acessar o arquivo `airflow.cfg` e configurar corretamente o path absoluto da pasta onde está o script exemplo.py na variavel dags folder, conforme exemplo abaixo:

	`dags_folder = /path/to/folder/machiron_exemplo_dag`

- É possível desabilitar os exemplos do Airflow através da variavel load_exemples

	`load_examples = False`

## Próximos passos

######  Nesse mesmo repositório iremos incluir scripts de tutorial com mais funcionalidades, e posteriormente iremos incluir exemplos com esteiras de machine learning e analise de dados.
