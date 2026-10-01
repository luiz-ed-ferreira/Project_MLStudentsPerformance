# Project Students Performance - Kaggle Dataset

### Project overview

> A machine learning project developed to explore and compare different predictive approaches, including Regression, Decision Trees, Neural Networks, and Genetic Algorithms. Based on a fictional dataset of high school student performance, the project involved data analysis, model development, and performance comparison to identify the most suitable approach for predicting student outcomes. This project was developed using Python and machine learning techniques.

### Status & improvements

In progress [developing]

- [x] Project structure definition
- [x] Dataset EDA
- [x] Baseline (linear regression) model studies
- [x] Causal inference studies
- [x] Decision tree model studies
- [x] Genetic algoritm model studies
- [x] Neural network model studies
- [x] Define and validate the model input schema
- [x] Review and serialize all trained ML models
- [ ] Implement centralized model loading
- [ ] Build a unified prediction layer for all models
- [ ] Handle the genetic algorithm feature selection pipeline
- [ ] Test the complete inference workflow
- [ ] Build the interactive Streamlit interface
- [ ] Create a model prediction and metrics dashboard
- [ ] Develop a REST API using FastAPI
- [ ] Connect Streamlit to the FastAPI backend
- [ ] Containerize the application with Docker
- [ ] Configure multi-container orchestration with Docker Compose
- [ ] Implement ML workflow orchestration with Apache Airflow
- [ ] Add automated tests and input validation
- [ ] Deploy the application and services on AWS
- [ ] Complete production documentation and architecture diagrams

### Model analyses

#### Objective

> The main objective is to predict students' Exam Score based on academic, behavioral, and demographic factors.

> The project also evaluates different Machine Learning approaches to answer: Which model provides the best predictive performance while maintaining an appropriate level of complexity?

#### Dataset

> The dataset contains 6,606 student observations and variables related to students' academic performance and personal habits (kaggle sample dataset).

- Target Variable
> Exam_Score

- Main Features

> Numerical:
>- Hours_Studied
>- Attendance
>- Sleep_Hours
>- Previous_Scores
>- Tutoring_Sessions
>- Physical_Activity

> Categorical:
>- The dataset also contains categorical variables related to factors such as parental involvement, education level, access to resources, motivation, teacher quality, and other student characteristics.

#### Exploratory data analysis & data preparation

> The project started with an Exploratory Data Analysis (EDA) to understand:

- Data distributions
- Missing values
- Numerical and categorical variables
- Potential outliers
- Relationships between variables and Exam_Score

> A total of 229 observations (3.47%) were removed.

> After preprocessing: 6,377 observations remained.

#### Models metrics result comparison table

<table>
  <thead>
    <tr>
      <th>Model</th>
      <th>MAE ↓</th>
      <th>RMSE ↓</th>
      <th>R² ↑</th>
      <th>Adjusted R² ↑</th>
      <th>Features</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Linear regression</strong></td>
      <td>0.48</td>
      <td><strong>2.04</strong></td>
      <td><strong>0.734</strong></td>
      <td><strong>0.730</strong></td>
      <td>40</td>
    </tr>
    <tr>
      <td>Decision tree</td>
      <td>1.83</td>
      <td>3.54</td>
      <td>0.199</td>
      <td>0.187</td>
      <td>40</td>
    </tr>
    <tr>
      <td>Tuned decision tree</td>
      <td>1.55</td>
      <td>2.69</td>
      <td>0.539</td>
      <td>0.532</td>
      <td>40</td>
    </tr>
    <tr>
      <td><strong>GA + Linear regression</strong></td>
      <td>~0.48</td>
      <td>~2.04</td>
      <td>~0.734</td>
      <td>~0.728</td>
      <td><strong>28</strong></td>
    </tr>
    <tr>
      <td>Neural network</td>
      <td>0.85</td>
      <td>2.20</td>
      <td>0.691</td>
      <td>0.686</td>
      <td>40</td>
    </tr>
    <tr>
      <td><strong>Tuned neural network</strong></td>
      <td><strong>0.46</strong></td>
      <td>2.05</td>
      <td>0.732</td>
      <td>0.728</td>
      <td>40</td>
    </tr>
  </tbody>
</table>
<br>

> Attention! <strong>↓ Lower is better &nbsp; | &nbsp; ↑ Higher is better</strong>

#### Key takeaways

##### Best MAE: Tuned Neural Network — 0.46

> The tuned neural network achieved the lowest average absolute prediction error.

##### Best RMSE & R²: Linear Regression — RMSE 2.04 / R² 0.734

> Despite being the simplest model, Linear Regression achieved the strongest overall performance across these metrics.

##### Best feature reduction: Genetic Algorithm — 40 -> 28 features

> The GA reduced the feature space by 30% while maintaining virtually the same predictive performance.

##### Best hyperparameter tuning: Decision Tree

> Hyperparameter tuning substantially improved the Decision Tree, but it remained less competitive than the other approaches.

#### Models conclusion

> One of the most interesting findings of this project was that greater model complexity did not necessarily lead to better predictive performance.
> Linear Regression provided an extremely strong baseline, while the tuned Neural Network achieved a slightly better MAE but similar overall performance.
> At the same time, the Genetic Algorithm demonstrated that the model could maintain comparable performance using 30% fewer features.
> Therefore, model selection should not rely exclusively on predictive accuracy. Performance, complexity, interpretability, and feature efficiency should all be considered when choosing a final model.

### Project evolution & architecture

> The next stage of this project focuses on transforming the Machine Learning experiments into an **end-to-end prediction application**.

> The goal is to allow users to enter student information through a **Streamlit interface**, run the trained Machine Learning models, and compare their predictions alongside the evaluation metrics obtained during model testing.

> The project will later evolve toward an API-based and containerized architecture using **FastAPI, Docker, Apache Airflow, and AWS**.

#### Planned architecture

```text
                         ┌──────────────────┐
                         │       User       │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │    Streamlit     │
                         │    Frontend      │
                         └────────┬─────────┘
                                  │
                             REST API
                                  │
                                  ▼
                         ┌──────────────────┐
                         │     FastAPI      │
                         │   ML Backend     │
                         └────────┬─────────┘
                                  │
              ┌───────────────────┼───────────────────┐
              │                   │                   │
              ▼                   ▼                   ▼
       Linear Models        Decision Trees      Neural Networks
              │                   │                   │
              └───────────────────┼───────────────────┘
                                  │
                                  ▼
                         Prediction Results
                                  │
                                  ▼
                         ┌──────────────────┐
                         │    Streamlit     │
                         │ Results Dashboard│
                         └──────────────────┘
```

#### Development roadmap

| Stage | Technology / Concept | Objective |
|---|---|---|
| 1 | Input Schema | Define and validate the student features required for prediction |
| 2 | Model Serialization | Save trained models and preprocessing pipelines for inference |
| 3 | Prediction Layer | Create a common function to execute all trained models |
| 4 | Streamlit | Build an interactive interface for student data input and prediction comparison |
| 5 | FastAPI | Expose the Machine Learning models through REST API endpoints |
| 6 | Docker | Containerize the application and its services |
| 7 | Apache Airflow | Orchestrate model training, evaluation, and retraining workflows |
| 8 | AWS | Deploy the application and ML services to cloud infrastructure |

---

#### Model input

> The prediction system receives **19 student features**.

> The target variable `Exam_Score` is not provided by the user, as it represents the value predicted by the Machine Learning models.

##### Numerical features

| Feature | Minimum | Maximum | Default |
|---|---:|---:|---:|
| `Hours_Studied` | 1 | 48 | 20 |
| `Attendance` | 60 | 100 | 80 |
| `Sleep_Hours` | 4 | 10 | 7 |
| `Previous_Scores` | 50 | 100 | 75 |
| `Tutoring_Sessions` | 0 | 8 | 1 |
| `Physical_Activity` | 0 | 6 | 3 |

##### Categorical features

| Feature | Accepted Values |
|---|---|
| `Parental_Involvement` | low, medium, high |
| `Access_to_Resources` | low, medium, high |
| `Extracurricular_Activities` | no, yes |
| `Motivation_Level` | low, medium, high |
| `Internet_Access` | no, yes |
| `Family_Income` | low, medium, high |
| `Teacher_Quality` | low, medium, high |
| `School_Type` | private, public |
| `Peer_Influence` | negative, neutral, positive |
| `Learning_Disabilities` | no, yes |
| `Parental_Education_Level` | high school, college, postgraduate |
| `Distance_from_Home` | near, moderate, far |
| `Gender` | female, male |

---

#### Prediction workflow

> The user inputs student information only once. The same observation is then processed by the trained models.

```text
Student Information
        │
        ▼
Input Validation
        │
        ▼
DataFrame
        │
        ▼
Preprocessing
        │
        ├──► Linear Regression
        ├──► Decision Tree
        ├──► Tuned Decision Tree
        ├──► GA + Linear Regression
        ├──► Neural Network
        └──► Tuned Neural Network
                    │
                    ▼
             Model Predictions
                    │
                    ▼
             Results Comparison
```

> The application will compare predictions from all models while also displaying their previously calculated test-set performance metrics:

- **MAE** — Mean Absolute Error
- **RMSE** — Root Mean Squared Error
- **R²** — Coefficient of Determination
- **Adjusted R²** — Adjusted Coefficient of Determination

> Performance metrics represent the models' historical performance on the test dataset and are not calculated from a single new user observation.

---

### Planned project structure

```text
Project_MLStudentsPerformance/
│
├── app/
│   └── streamlit_app.py
│
├── docs/
│   └── Models_project_structure.txt
│
├── models/
│   ├── baseline.pkl
│   ├── decision_tree.pkl
│   ├── tuned_decision_tree.pkl
│   ├── genetic_algorithm_linear_regression.pkl
│   ├── neural_network.pkl
│   └── tuned_neural_network.pkl
│
├── models_notebooks/
│   ├── baseline.ipynb
│   ├── decision_tree.ipynb
│   ├── genetic_algorithm.ipynb
│   └── neural_network.ipynb
│
├── notebooks/
│   ├── causal_inference.ipynb
│   └── main_analyses.ipynb
│
├── src/
│   ├── config.py
│   ├── input_schema.py
│   ├── model_loader.py
│   ├── prediction.py
|   ├── preprocessing.py  
│   └── training_test_variables_80_20.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

> This architecture separates **data processing, model inference, user interface, and infrastructure**, making the project easier to maintain and allowing each component to evolve independently.

### Prerequisites & used softwares

- WSL Linux/Ubuntu for Windows 11 System
- Python version 3.12.3
- Streamlit 1.64.0
- FastAPI 0.142.2
- Docker 4.93.0
- Apache Airflow 3.3.2

> Attention! Consult the requirements.txt file for more information about python libraries used.

### Collaborators

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/luiz-ed-ferreira" title="Luiz Eduardo">
        <img src="https://avatars3.githubusercontent.com/u/145693602" width="100px;" alt="Foto do Iuri Silva no GitHub"/><br>
        <sub>
          <b>Luiz Eduardo</b>
        </sub>
      </a>
    </td>
</table>
