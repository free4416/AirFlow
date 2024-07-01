from airflow import DAG
import pendulum
import datetime
from airflow.operators.email import EmailOperator

with DAG(
    dag_id = "dags_email_operator",
    schedule="0 8 1 * *",
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    
    send_email_task = EmailOperator(
        task_id = "send_email_task",
        to="free4416@naver.com",
        cc="woojug.song.83@gmail.com",
        subject="AirFlow EmailOperator Success",
        html_content="AirFlow 메일발송을 성공 하였습니다. 축하축하!!"
    )


