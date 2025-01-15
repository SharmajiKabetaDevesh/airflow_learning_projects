from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

#define the task
def preprocess_data():
    print("Preprocessing the data/...")

def train_model():
    print("Training the data")

def evaluate_model():
    print("Evaluating the model")


#define the dag here

with DAG (
    "ml_pipeline",
    start_date=datetime(2025,1,14),
    schedule_interval='@daily',
    catchup=False

)as dag:
    #define the task
    preprocess=PythonOperator(task_id="preprocess" ,python_callable = preprocess_data)
    train=PythonOperator(task_id="train",python_callable= train_model)
    evaluate=PythonOperator(task_id="evaluate",python_callable=evaluate_model)

    preprocess >> train >> evaluate