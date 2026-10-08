#Initializers (bash)
    #->uvicorn api.main:app --reload
    #->streamlit run app/streamlit_app.py

#Call libraries
from pathlib import Path
import streamlit as st 
import pandas as pd
import requests
import os

#Attention -> Streamlit should no longer directly access ML layer more
    #Call prediction function from src/prediction.py (definition of root folder to import src folder)
    #PROJECT_ROOT = Path(__file__).resolve().parent.parent
    #if str(PROJECT_ROOT) not in sys.path:
    #    sys.path.insert(0, str(PROJECT_ROOT))
    #from src.prediction import predict_all_models 

#API URL for the FastAPI backend (API)
    #API_URL = "http://127.0.0.1:8000" 

#Create environment variable for API URL (docker)
API_URL = os.getenv(
    "API_URL",
    "http://127.0.0.1:8000",
)

#----------------------------------------------------------

st.set_page_config(
    page_title="Project Students Performance - MLOps Predictor",
    page_icon="🎓",
    layout="wide",
)

#----------------------------------------------------------

st.title("🎓 Project Students Performance - MLOps Predictor")

st.write(
    "*Created by Luiz Eduardo Ferreira - Data Scientist & MLOps Engineer.* "
)
st.write(
    "Enter the student's information below to estimate the exam score "
    "using multiple Machine Learning models."
)

#----------------------------------------------------------

#Academic information
st.subheader("📚 Academic Information")
with st.expander("Click here to view the options"):
    col1, col2 = st.columns(2)

    with col1:
        hours_studied = st.slider(
            "Hours Studied",
            min_value=1,
            max_value=48,
            value=20,
        )

        previous_scores = st.slider(
            "Previous Scores",
            min_value=50,
            max_value=100,
            value=75,
        )

    with col2:
        attendance = st.slider(
            "Attendance (%)",
            min_value=60,
            max_value=100,
            value=80,
        )

        tutoring_sessions = st.slider(
            "Tutoring Sessions",
            min_value=0,
            max_value=8,
            value=1,
        )

#----------------------------------------------------------

#Student profile
st.subheader("👤 Student Profile")
with st.expander("Click here to view the options"):
    col1, col2 = st.columns(2)
    with col1:
        motivation_level = st.selectbox(
            "Motivation Level",
            ["low", "medium", "high"],
            index=1,
        )

        sleep_hours = st.slider(
            "Sleep Hours",
            min_value=4,
            max_value=10,
            value=7,
        )

        extracurricular_activities = st.selectbox(
            "Extracurricular Activities",
            ["no", "yes"],
            index=1,
        )

    with col2:
        physical_activity = st.slider(
            "Physical Activity",
            min_value=0,
            max_value=6,
            value=3,
        )

        learning_disabilities = st.selectbox(
            "Learning Disabilities",
            ["no", "yes"],
        )

        gender = st.selectbox(
            "Gender",
            ["female", "male"],
        )

#----------------------------------------------------------

#School and resources
st.subheader("🏫 School & Resources")
with st.expander("Click here to view the options"):
    col1, col2 = st.columns(2)
    with col1:
        school_type = st.selectbox(
            "School Type",
            ["private", "public"],
        )

        teacher_quality = st.selectbox(
            "Teacher Quality",
            ["low", "medium", "high"],
            index=1,
        )

        access_to_resources = st.selectbox(
            "Access to Resources",
            ["low", "medium", "high"],
            index=1,
        )

    with col2:
        internet_access = st.selectbox(
            "Internet Access",
            ["no", "yes"],
            index=1,
        )

        distance_from_home = st.selectbox(
            "Distance from Home",
            ["near", "moderate", "far"],
            index=1,
        )

#----------------------------------------------------------

#Social and family information
st.subheader("👨‍👩‍👧 Social & Family Information")
with st.expander("Click here to view the options"):
    col1, col2 = st.columns(2)
    with col1:
        parental_involvement = st.selectbox(
            "Parental Involvement",
            ["low", "medium", "high"],
            index=1,
        )

        parental_education_level = st.selectbox(
            "Parental Education Level",
            ["high school", "college", "postgraduate"],
            index=1,
        )

    with col2:
        family_income = st.selectbox(
            "Family Income",
            ["low", "medium", "high"],
            index=1,
        )

        peer_influence = st.selectbox(
            "Peer Influence",
            ["negative", "neutral", "positive"],
            index=1,
        )

#----------------------------------------------------------

#Prediction results
st.divider()
if st.button(
    "Predict Exam Score",
    type="primary",
    use_container_width=True,
):

    student_data = {
        "Hours_Studied": hours_studied,
        "Attendance": attendance,
        "Parental_Involvement": parental_involvement,
        "Access_to_Resources": access_to_resources,
        "Extracurricular_Activities": extracurricular_activities,
        "Sleep_Hours": sleep_hours,
        "Previous_Scores": previous_scores,
        "Motivation_Level": motivation_level,
        "Internet_Access": internet_access,
        "Tutoring_Sessions": tutoring_sessions,
        "Family_Income": family_income,
        "Teacher_Quality": teacher_quality,
        "School_Type": school_type,
        "Peer_Influence": peer_influence,
        "Physical_Activity": physical_activity,
        "Learning_Disabilities": learning_disabilities,
        "Parental_Education_Level": parental_education_level,
        "Distance_from_Home": distance_from_home,
        "Gender": gender,
    }
    try:
        #Attention -> Streamlit should no longer directly access ML layer more
            #predictions = predict_all_models(student_data)

        #Attetion -> Now, here is the response from the FastAPI backend
        response = requests.post(
            f"{API_URL}/predict",
            json=student_data,
            timeout=30,
        )
        response.raise_for_status()
        result = response.json()
        predictions = result["predictions"]
           
        st.success("Predictions generated successfully.")
        st.subheader("📊 Model Predictions")

        columns = st.columns(len(predictions))

        for column, (model_name, prediction) in zip(
            columns,
            predictions.items()
        ):
            with column:
                st.metric(
                    label=model_name.replace("_", " ").title(),
                    value=f"{prediction:.2f}",
                )
    #API errors
    except requests.exceptions.ConnectionError:
        st.error(
            "Could not connect to the prediction API. "
            "Please make sure the FastAPI service is running."
        )
    except requests.exceptions.Timeout:
        st.error(
            "The prediction API took too long to respond."
        )
    except requests.exceptions.RequestException as error:
        st.error(
            f"API request failed: {error}"
        )
    except Exception as error:
        st.error(
            f"Unexpected error: {error}"
        )

#----------------------------------------------------------

#Metrics comparison
    MODEL_DISPLAY_NAMES = {
        "baseline": "Linear Regression",
        "decision_tree": "Decision Tree",
        "tuned_decision_tree": "Tuned Decision Tree",
        "genetic_algorithm": "GA + Linear Regression",
        "neural_network": "Neural Network",
        "tuned_neural_network": "Tuned Neural Network",
    }

    MODEL_METRICS = {
        "baseline": {
            "MAE": 0.480,
            "RMSE": 2.040,
            "R²": 0.734,
            "Adjusted R²": 0.730,
        },
        "decision_tree": {
            "MAE": 1.830,
            "RMSE": 3.540,
            "R²": 0.199,
            "Adjusted R²": 0.187,
        },
        "tuned_decision_tree": {
            "MAE": 1.550,
            "RMSE": 2.690,
            "R²": 0.539,
            "Adjusted R²": 0.532,
        },
        "genetic_algorithm": {
            "MAE": 0.477,
            "RMSE": 2.039,
            "R²": 0.7344,
            "Adjusted R²": 0.728,
        },
        "neural_network": {
            "MAE": 0.850,
            "RMSE": 2.200,
            "R²": 0.691,
            "Adjusted R²": 0.686,
        },
        "tuned_neural_network": {
            "MAE": 0.460,
            "RMSE": 2.050,
            "R²": 0.732,
            "Adjusted R²": 0.728,
        },
    }

    with st.expander("📈 Model Performance Comparison"):
        metrics_data = []
        for model_name, metrics in MODEL_METRICS.items():
            metrics_data.append(
                {
                    "Model": MODEL_DISPLAY_NAMES[model_name],
                    "MAE": metrics["MAE"],
                    "RMSE": metrics["RMSE"],
                    "R²": metrics["R²"],
                    "Adjusted R²": metrics["Adjusted R²"],
                }
            )
        metrics_df = pd.DataFrame(metrics_data)

        st.dataframe(
            metrics_df,
            use_container_width=True,
            hide_index=True,
        )

        st.caption(
            "MAE and RMSE: lower values indicate better performance. "
            "R² and Adjusted R²: higher values indicate better performance."
        )

        #Graphs comparison
        st.divider()
        
        st.markdown("#### Error Metrics")

        error_metrics_df = metrics_df.set_index("Model")[
            ["MAE", "RMSE"]
        ]

        st.bar_chart(
            error_metrics_df,
            use_container_width=True,
        )

        st.caption(
            "Lower MAE and RMSE values indicate better predictive performance."
        )

        st.markdown("#### Model Fit Metrics")

        fit_metrics_df = metrics_df.set_index("Model")[
            ["R²", "Adjusted R²"]
        ]

        st.bar_chart(
            fit_metrics_df,
            use_container_width=True,
        )

        st.caption(
            "Higher R² and Adjusted R² values indicate better model fit."
        )

#----------------------------------------------------------