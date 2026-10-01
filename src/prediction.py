#Call libraries
from typing import Any
import pandas as pd
from src.input_schema import INPUT_FEATURES, validate_input
from src.model_loader import load_models

#----------------------------------------------------------

#Function to create a DataFrame from the student input data, ensuring that the features are ordered according to the model's expected input schema. It first validates the input data and then constructs a DataFrame with one observation
def create_input_dataframe(student_data: dict[str, Any]) -> pd.DataFrame:
    """
        Convert student input data into a DataFrame compatible with the models

        Args:
            student_data: Dictionary containing student feature values

        Returns:
            DataFrame containing one student observation
    """

    validate_input(student_data)

    ordered_data = {
        feature: student_data[feature]
        for feature in INPUT_FEATURES
    }

    return pd.DataFrame([ordered_data])

#----------------------------------------------------------

#Function to generate predictions for a single model based on the provided student input data. It first converts the input data into a DataFrame and then uses the specified model to make a prediction, returning the predicted Exam Score as a float
def predict_all_models(student_data: dict[str, Any]) -> dict[str, float]:
    """
        Generate Exam Score predictions using all available models

        Args:
            student_data: Dictionary containing student feature values

        Returns:
            Dictionary containing the prediction from each model
    """

    student_df = create_input_dataframe(student_data)

    models = load_models()

    predictions = {}

    for model_name, model in models.items():
        prediction = model.predict(student_df)[0]

        predictions[model_name] = float(prediction)

    return predictions

#----------------------------------------------------------