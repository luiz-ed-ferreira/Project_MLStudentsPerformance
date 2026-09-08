# Project students performance - Kaggle dataset

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
- [ ] TBD

> Attention! Consult the Project_structure.txt file for more information on the project pipeline.

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

### Prerequisites & used softwares

- WSL Linux/Ubuntu for Windows 11 System
- Python version 3.12.3

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
