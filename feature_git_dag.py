#from airflow.models.dag import DAG
from .py_utils.dags_model import HtgDAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
import pendulum
import datetime

with HtgDAG(
    dag_id="feature_git_dag",
    severity=3,
    slack_alerts_channel_name="",
    model_name="",
    schedule=None,
    start_date=pendulum.datetime(2024, 10, 13, tz="UTC"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["local", "test"],
) as dag:

    run_this = BashOperator(
        task_id="print_var",
        bash_command="echo Feature - {{ var.value.get('TEST_VAR') }}",
    )
    

