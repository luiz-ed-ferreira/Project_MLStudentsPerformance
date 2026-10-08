#Attention -> This file is used for testing the prediction function. It is not part of the main application code

#Call libraries
import sys
sys.path.append("../")
from src.prediction import predict_all_models

#----------------------------------------------------------

#JSON input data for testing the prediction function
student_data = {
    "Hours_Studied": 20,
    "Attendance": 80,
    "Parental_Involvement": "medium",
    "Access_to_Resources": "medium",
    "Extracurricular_Activities": "yes",
    "Sleep_Hours": 7,
    "Previous_Scores": 75,
    "Motivation_Level": "medium",
    "Internet_Access": "yes",
    "Tutoring_Sessions": 1,
    "Family_Income": "medium",
    "Teacher_Quality": "medium",
    "School_Type": "public",
    "Peer_Influence": "neutral",
    "Physical_Activity": 3,
    "Learning_Disabilities": "no",
    "Parental_Education_Level": "college",
    "Distance_from_Home": "moderate",
    "Gender": "male",
}

#----------------------------------------------------------

#Result of the prediction function
predictions = predict_all_models(student_data)
print("\nStudent Performance Predictions")
print("=" * 40)
for model_name, prediction in predictions.items():
    print(
        f"{model_name:<30} "
        f"{prediction:.2f}"
    )

#----------------------------------------------------------