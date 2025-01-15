from airflow import DAG
from airflow.operators.python import PythonOperator  
from datetime import datetime

# Define the task functions
def start_number(**context):
    context["ti"].xcom_push(key="curr_value", value=10)  
    print("Starting with the number")

def add_five(**context):
    current_value = context["ti"].xcom_pull(key="curr_value", task_ids='start_task')
    new_value = current_value + 5
    context["ti"].xcom_push(key="curr_value", value=new_value)

def multiply(**context):
    current_value = context["ti"].xcom_pull(key="curr_value", task_ids='add_task')
    new_value = current_value * 2
    context["ti"].xcom_push(key="curr_value", value=new_value)

def subtract(**context):
    current_value = context["ti"].xcom_pull(key="curr_value", task_ids='mul_task')
    new_value = current_value - 3
    context["ti"].xcom_push(key="curr_value", value=new_value)  


with DAG(
    dag_id='performing_math_opr_sequentially',
    start_date=datetime(2025, 1, 14),
    schedule_interval='@once',
    catchup=False
) as dag:
    
    start_task = PythonOperator(
        task_id='start_task',
        python_callable=start_number,
        provide_context=True
    )
    
    add_task = PythonOperator(  
        task_id="add_task",  
        python_callable=add_five,
        provide_context=True
    )
    
    mul_task = PythonOperator(  
        task_id="mul_task", 
        python_callable=multiply,
        provide_context=True
    )
    
    subtract_task = PythonOperator(  
        task_id="subtract_task",  
        python_callable=subtract,
        provide_context=True
    )

    
    start_task >> add_task >> mul_task >> subtract_task
