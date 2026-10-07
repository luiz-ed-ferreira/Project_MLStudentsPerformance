#Uses Python 3.12 as the base image
FROM python:3.12-slim

#Defines the working directory inside the container
WORKDIR /app

#Copies the dependency file
COPY requirements.txt .

#Installs the project dependencies.
RUN pip install --no-cache-dir -r requirements.txt

#Copies the Streamlit application
COPY app/ ./app/

#Documents the port used by Streamlit
EXPOSE 8501

#Starts the Streamlit application.
CMD ["streamlit", "run", "app/streamlit_app.py", "--server.address=0.0.0.0", "--server.port=8501"]