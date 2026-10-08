#call libraries
import json
import joblib
from src.config import TRAINING_OUTPUT_DIR
from pathlib import Path
from typing import Any

#----------------------------------------------------------

#Funtion to save the trained model in .pkl format
def save_model(model: Any, filename: str,) -> Path:
    """ Save a trained machine learning model. """
    TRAINING_OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    model_path = TRAINING_OUTPUT_DIR / filename
    joblib.dump(model, model_path)

    return model_path

#----------------------------------------------------------

#Funtion to save the model evaluation metrics in .json format
def save_metrics(metrics: dict[str, float], filename: str) -> Path:
    """ Save model evaluation metrics as a JSON file. """
    TRAINING_OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )
    #Note -> This ensures that the output folder is automatically created if it does not already exist
    
    metrics_path = TRAINING_OUTPUT_DIR / filename
    with metrics_path.open(
        mode="w",
        encoding="utf-8",
    ) as file:
        json.dump(
            metrics,
            file,
            indent=4,
            allow_nan=False,
        )

    return metrics_path

#----------------------------------------------------------
