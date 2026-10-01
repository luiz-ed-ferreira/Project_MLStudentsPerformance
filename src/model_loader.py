#Call libraries
from pathlib import Path
from typing import Any
import joblib
import sys
sys.path.append("../")

#----------------------------------------------------------

#Create a constant variable to store the path to the models directory and a dictionary to map model names to their corresponding file names
PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODELS_DIR = PROJECT_ROOT / "models"

#Pkl files catalog
MODEL_FILES: dict[str, str] = {
    "baseline": "baseline.pkl",
    "decision_tree": "decision_tree.pkl",
    "tuned_decision_tree": "tuned_decision_tree.pkl",
    "genetic_algorithm": "genetic_algorithm_linear_regression.pkl",
    "neural_network": "neural_network.pkl",
    "tuned_neural_network": "tuned_neural_network.pkl",
}

#----------------------------------------------------------

#Function to load a serialized machine learning model from the models directory based on the provided model name. It raises a ValueError if the model name is not registered and a FileNotFoundError if the model file does not exist
def load_model(model_name: str) -> Any:
    """
        Load a serialized machine learning model

        Args:
            model_name: Name of the model to load

        Returns:
            Loaded machine learning model

        Raises:
            ValueError: If the model name is not registered
            FileNotFoundError: If the model file does not exist
    """

    if model_name not in MODEL_FILES:
        raise ValueError(
            f"Unknown model: '{model_name}'. "
            f"Available models: {list(MODEL_FILES.keys())}"
        )

    model_path = MODELS_DIR / MODEL_FILES[model_name]

    if not model_path.exists():
        raise FileNotFoundError(
            f"Model file not found: {model_path}"
        )

    return joblib.load(model_path)

#----------------------------------------------------------

#Function to load all registered machine learning models from the models directory and return them as a dictionary where the keys are the model names and the values are the loaded models
def load_models() -> dict[str, Any]:
    """
        Load all registered machine learning models

        Returns:
            Dictionary containing all loaded models
    """

    return {
        model_name: load_model(model_name)
        for model_name in MODEL_FILES
    }

#----------------------------------------------------------