#Call libraries
from datetime import datetime
from airflow.sdk import dag, task #Imports the DAG and Task decorators from Apache Airflow 3

#Defines a DAG using the TaskFlow API
#A DAG (Directed Acyclic Graph) represents a workflow composed of tasks and their execution dependencies
@dag(
    #Unique identifier displayed in the Airflow UI
    dag_id="student_performance_baseline_training",

    #Earliest logical date from which the DAG can be scheduled
    #This does not automatically trigger a DAG execution
    start_date=datetime(2026, 10, 1),

    #Disables automatic scheduling
    #The DAG will only run when manually triggered or via the API
    schedule=None,

    #Prevents Airflow from automatically creating historical runs for missed scheduled intervals
    catchup=False,

    #Labels used to organize and filter DAGs in the Airflow UI
    tags=["machine-learning", "training"],
)
def baseline_training_pipeline():
    """ Define the workflow for training the baseline Student Performance regression model. """

    #Converts this Python function into an Airflow task
    #Airflow manages its execution, state, logs, and retries
    @task
    def train_baseline_model():
        """ Execute the complete baseline ML training pipeline. """
        #Imports the training entry