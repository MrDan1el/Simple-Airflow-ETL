from datetime import datetime
from airflow.models import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator


default_args = {
    "owner": "username",
    "depends_on_past": False,
    "start_date": datetime(2024, 12, 16)
}

dag = DAG(
    dag_id='from_api_to_pg', 
    default_args=default_args, 
    schedule_interval='0 1 * * *', 
    catchup=True,
    tags=["etl", "api", "postgres"]
)

start = EmptyOperator(
    task_id="start"
)

start_python_script = BashOperator(
    task_id='start_python_script',
    bash_command='python3 /scripts/run.py',
    dag=dag
)

end = EmptyOperator(
    task_id="end"
) 
   
start >> start_python_script >> end