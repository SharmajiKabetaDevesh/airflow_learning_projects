from airflow import DAG
from airflow.operator.pythonoperator import PythonOperator
from airflow.operators.python import PythonOperator  
from airflow.decorators import task
from datetime import datetime



with DAG(
    dag_id="usingtaskdecorator",
    start_date=datetime(2025,1,14),
    schedule_interval="@once",
    catchup=False
)as dag:
    @task
    def start_number():
        initial_value = 10
        print("Starting with the number")
        return initial_value
    
    @task
    def add_five(current_value):
        new_value = current_value + 5
        return new_value
    
    @task
    def multiply(current_value):
        new_value = current_value * 2
        return new_value
    
    @task
    def subtract(current_value):
        new_value = current_value - 3
        return new_value
    
    @task
    def square(current_value):
        return current_value ** 2
    
    start=start_number()
    add=add_five(start)
    mul=multiply(add)
    sub=subtract(mul)
    square=subtract(sub)

    
