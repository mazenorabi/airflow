from airflow.models import DAG
from datetime import datetime

class HtgDAG(DAG):
        def __init__(self,
                 dag_id: str,
                 severity: int,
                 slack_alerts_channel_name: str,
                 model_name: str,
                 default_args: dict = None,
                 **kwargs):
        self.model_name = model_name
        
        if default_args is None:
            default_args = {}
        
        default_args['severity'] = severity
        default_args['slack_alerts_channel_name'] = slack_alerts_channel_name
        today = datetime.now().strftime('%Y%m%d')
        super().__init__(
            dag_id=f"tst.{dag_id}.{today}",
            default_args=default_args,
            **kwargs,
        )
