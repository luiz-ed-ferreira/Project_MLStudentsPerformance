#Call librarie
from typing import Any

#----------------------------------------------------------

#Features definition
#Stores the rules for the 6 numerical variables
NUMERICAL_FEATURES: dict[str, dict[str, int]] = {
    "Hours_Studied": {
        "min": 1,
        "max": 48,
        "default": 20,
    },
    "Attendance": {
        "min": 60,
        "max": 100,
        "default": 80,
    },
    "Sleep_Hours": {
        "min": 4,
        "max": 10,
        "default": 7,
    },
    "Previous_Scores": {
        "min": 50,
        "max": 100,
        "default": 75,
    },
    "Tutoring_Sessions": {
        "min": 0,
        "max": 8,
        "default": 1,
    },
    "Physical_Activity": {
        "min": 0,
        "max": 6,
        "default": 3,
    },
}

#Stores the valid values ​​of the 13 categorical variables
CATEGORICAL_FEATURES: dict[str, list[str]] = {
    "Parental_Involvement": [
        "low",
        "medium",
        "high",
    ],
    "Access_to_Resources": [
        "low",
        "medium",
        "high",
    ],
    "Extracurricular_Activities": [
        "no",
        "yes",
    ],
    "Motivation_Level": [
        "low",
        "medium",
        "high",
    ],
    "Internet_Access": [
        "no",
        "yes",
    ],
    "Family_Income": [
        "low",
        "medium",
        "high",
    ],
    "Teacher_Quality": [
        "low",
        "medium",
        "high",
    ],
    "School_Type": [
        "private",
        "public",
    ],
    "Peer_Influence": [
        "negative",
        "neutral",
        "positive",
    ],
    "Learning_Disabilities": [
        "no",
        "yes",
    ],
    "Parental_Education_Level": [
        "high school",
        "college",
        "postgraduate",
    ],
    "Distance_from_Home": [
        "near",
        "moderate",
        "far",
    ],
    "Gender": [
        "female",
        "male",
    ],
}

#Definition of the 19 columns and their original order
INPUT_FEATURES: list[str] = [
    "Hours_Studied",
    "Attendance",
    "Parental_Involvement",
    "Access_to_Resources",
    "Extracurricular_Activities",
    "Sleep_Hours",
    "Previous_Scores",
    "Motivation_Level",
    "Internet_Access",
    "Tutoring_Sessions",
    "Family_Income",
    "Teacher_Quality",
    "School_Type",
    "Peer_Influence",
    "Physical_Activity",
    "Learning_Disabilities",
    "Parental_Education_Level",
    "Distance_from_Home",
    "Gender",
]

#Definition of the target Exam_Score
TARGET: str = "Exam_Score"

#----------------------------------------------------------

#To validate categorical and numerical variable inputs (both: Streamlit and FastAPI)
def validate_input(student_data: dict[str, Any]) -> None:
    """
        Validate student input data against the model input schema

        Args:
            student_data: Dictionary containing student feature values

        Raises:
            ValueError: If a feature is missing or contains an invalid value
    """

    missing_features = [
        feature
        for feature in INPUT_FEATURES
        if feature not in student_data
    ]

    if missing_features:
        raise ValueError(
            f"Missing input features: {missing_features}"
        )

    for feature, constraints in NUMERICAL_FEATURES.items():
        value = student_data[feature]

        if not isinstance(value, (int, float)):
            raise ValueError(
                f"{feature} must be numeric."
            )

        if not constraints["min"] <= value <= constraints["max"]:
            raise ValueError(
                f"{feature} must be between "
                f"{constraints['min']} and {constraints['max']}."
            )

    for feature, allowed_values in CATEGORICAL_FEATURES.items():
        value = student_data[feature]

        if value not in allowed_values:
            raise ValueError(
                f"{feature} must be one of {allowed_values}."
            )

#----------------------------------------------------------

#Notes:
    #Streamlit input schema features/variables

    #Call libraries
    #import pandas as pd

    #Transformed dataset (from EDA)
    #Students performance factors for model dataset
    #student_performance_factors_for_model = pd.read_csv('data/student_performance_factors_for_model.csv')

    #Without Exam_Score
    #X = student_performance_factors_for_model.drop(columns=['Exam_Score'])

    #Columns type identification
    #Categorical collumns
    #categorical_columns = X.select_dtypes(
    #    include=["object", "string"]
    #).columns.tolist() #-> 14

    #for column in categorical_columns:
    #    print(f"\n{column}")
    #    print(sorted(X[column].dropna().unique()))

    #Numerical collumns
    #numerical_input_columns = [
    #    "Hours_Studied",
    #    "Attendance",
    #    "Sleep_Hours",
    #    "Previous_Scores",
    #    "Tutoring_Sessions",
    #    "Physical_Activity"
    #]

    #print(
    #    X[numerical_input_columns]
    #    .agg(["min", "max", "median"])
    #    .T
    #)