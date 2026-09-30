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

#After reading the dataset
NUMERICAL_FEATURES = {
    "Hours_Studied": {
        "min": 1,
        "max": 48, #-> two days
        "default": 20
    },
    "Attendance": {
        "min": 60,
        "max": 100,
        "default": 80
    },
    "Sleep_Hours": {
        "min": 4,
        "max": 10,
        "default": 7
    },
    "Previous_Scores": {
        "min": 50,
        "max": 100,
        "default": 75
    },
    "Tutoring_Sessions": {
        "min": 0,
        "max": 8,
        "default": 1
    },
    "Physical_Activity": {
        "min": 0,
        "max": 6,
        "default": 3
    }
}

CATEGORICAL_FEATURES = {
    "Parental_Involvement": ["low", "medium", "high"],
    "Access_to_Resources": ["low", "medium", "high"],
    "Extracurricular_Activities": ["no", "yes"],
    "Motivation_Level": ["low", "medium", "high"],
    "Internet_Access": ["no", "yes"],
    "Family_Income": ["low", "medium", "high"],
    "Teacher_Quality": ["low", "medium", "high"],
    "School_Type": ["private", "public"],
    "Peer_Influence": ["negative", "neutral", "positive"],
    "Learning_Disabilities": ["no", "yes"],
    "Parental_Education_Level": ["high school", "college", "postgraduate"],
    "Distance_from_Home": ["near", "moderate","far"],
    "Gender": ["female","male"]
}