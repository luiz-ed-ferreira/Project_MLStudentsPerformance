#Call libraries
import os
import subprocess
import sys
from datetime import datetime
from airflow.sdk import dag, task #Imports the DAG and Task decorators from Apache Airflow 3

#Airflow path to the ML project directory
ML_PROJECT_DIR = "/opt/airflow/ml_project"

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
    """ Orchestrate baseline model training. """

    #Converts this Python function into an Airflow task
    @task
    def train_baseline_model():
        """ Run the ML training pipeline in an isolated process. """

        environment = os.environ.copy()
        environment["PYTHONPATH"] = ML_PROJECT_DIR

        subprocess.run(
            [
                sys.executable,
                "-m",
                "src.training.run_training",
            ],
            cwd=ML_PROJECT_DIR,
            env=environment,
            check=True,
        )
    train_baseline_model()

baseline_training_pipeline()