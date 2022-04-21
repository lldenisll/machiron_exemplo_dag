from airflow import DAG 
from datetime import datetime
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
import requests
import json
import random

def escolhe_pokemon():
    pokemons = ['bulbasaur', 'charmander', 'squirtle']
    url = "https://pokeapi.co/api/v2/pokemon/{}/".format(random.choice(pokemons))
    response = requests.get(url)
    pokemon = response.json()
    print(pokemon['name'])
    return pokemon['name']

def se_charmander(ti):
    pokemon = ti.xcom_pull(task_ids='escolhe_pokemon')
    if pokemon == "charmander":
        return('e_charmander')
    return('n_charmander')
    
with DAG('exemplo',start_date=datetime(2022,1,1),schedule_interval='30 * * * *') as dag:

    escolhe_pokemon = PythonOperator(
        task_id='escolhe_pokemon', 
        python_callable=escolhe_pokemon
        )

    se_charmander=BranchPythonOperator(
        task_id='se_charmander',
        python_callable=se_charmander,
    )

    e_charmander=BashOperator(
        task_id='e_charmander',
        bash_command="echo 'É o charmander'"
    )

    n_charmander=BashOperator(
        task_id='n_charmander',
        bash_command="echo 'Não é o charmander'"
    )


escolhe_pokemon >> se_charmander >> [e_charmander, n_charmander]