#Call libraries
from pathlib import Path

#----------------------------------------------------------
#Project paths
#----------------------------------------------------------

#Absolute path to the project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

#Directory containing the original datasets
DATA_DIR = PROJECT_ROOT / "data"

#Directory containing production-ready ML models
MODELS_DIR = PROJECT_ROOT / "models"

#Directory for newly trained models and evaluation artifacts
TRAINING_OUTPUT_DIR = PROJECT_ROOT / "training_outputs"

#----------------------------------------------------------
#Dataset configuration
#----------------------------------------------------------

#Target variable used for supervised learning
TARGET = "Exam_Score"

#Name of the original dataset
DATASET_FILENAME = "../data/student_performance_factors_for_model.csv"

#----------------------------------------------------------
#Machine learning configuration
#----------------------------------------------------------

#Percentage of data reserved for model evaluation.
TEST_SIZE = 0.20

#Random seed for reproducible experiments.
RANDOM_STATE = 42

#Notes: 
    #Considering (for a good performance):
        #80% -> Training
        #20% -> Test
    #RANDOM_STATE=42 does not improve the model. It merely ensures that the randomness is reproducible
    #For other definitions 42 is "life, the universe, and everything else

#----------------------------------------------------------
#Training artifacts
#----------------------------------------------------------

#Filename used when saving a newly trained baseline model
BASELINE_MODEL_FILENAME = "baseline.pkl"

#Filename used when saving baseline evaluation metrics
BASELINE_METRICS_FILENAME = "baseline_metrics.json"

#----------------------------------------------------------
