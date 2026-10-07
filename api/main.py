#Initializers (bash)
    #->uvicorn api.main:app --reload

#Call libraries
from fastapi import FastAPI
import sys
sys.path.append("../")
from fastapi import FastAPI, HTTPException
from src.input_schema import StudentInput
from src.prediction import predict_all_models

#----------------------------------------------------------
#/docs - swagger (test)

#Copyright message
app = FastAPI(
    title="Project Students Performance - MLOps Predictor",
    description=(
        "REST API for predicting student exam performance "
        "using multiple Machine Learning models. "
        "*Created by Luiz Eduardo Ferreira - Data Scientist & MLOps Engineer.* "
    ),
    version="1.0.0",
)

#Commit/root message
@app.get("/")
def root() -> dict[str, str]:
    return {
        "message": "Student Performance API is running."
    }

#Status message
@app.get("/health")
def health_check() -> dict[str, str]:
    return {
        "status": "healthy"
    }

#Endpoint to predict student performance
@app.post("/predict")
def predict(student: StudentInput) -> dict:
    try:
        #Pydantic receives the JSON from the request and creates a StudentInput object. 
        #model_dump() converts this object back into a dict compatible with our existing function.
        predictions = predict_all_models(
            student.model_dump()
        )

        return {
            "predictions": predictions
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error),
        ) from error