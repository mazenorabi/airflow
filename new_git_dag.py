from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
import pendulum
import datetime

with DAG(
    dag_id="new_git_dag",
    schedule=None,
    start_date=pendulum.datetime(2024, 10, 13, tz="UTC"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["local", "test"],
    #params={"example_key": "example_value"},
) as dag:

    run_this = BashOperator(
        task_id="print_var",
        bash_command="echo Testing - {{ var.value.get('TEST_VAR') }}",
    )
    

