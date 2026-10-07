#Uses the official Python 3.12 slim image as the base image
#The slim version is smaller because it contains only essential system packages
FROM python:3.12-slim

#Defines /app as the working directory inside the container
#The following commands will be executed relative to this directory
WORKDIR /app

#Copies the project's dependency file into the container
COPY requirements.txt .

#Installs all Python dependencies required by the project
#--no-cache-dir prevents pip from storing installation cache, helping reduce the final Docker image size
RUN pip install --no-cache-dir -r requirements.txt

#Copies the ML application source code into the container
COPY src/ ./src/

#Copies the FastAPI application into the container
COPY api/ ./api/

#Copies the serialized Machine Learning models into the container
COPY models/ ./models/

#Documents that the application inside the container uses port 8000
#FastAPI/Uvicorn will listen on this port
EXPOSE 8000

#Defines the command executed when the container starts:
    #Equivalent terminal command -> uvicorn api.main:app --host 0.0.0.0 --port 8000
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
#api.main:app means:
    #api      -> api package
    #main     -> main.py module
    #app      -> FastAPI application object
    #0.0.0.0  -> Allows the API to receive connections from outside the container