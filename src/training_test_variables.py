#Call libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from src.config import RANDOM_STATE, TEST_SIZE

#----------------------------------------------------------

#Transformed dataset (from EDA)
#Students performance factors for model dataset
student_performance_factors_for_model = pd.read_csv('../data/student_performance_factors_for_model.csv')

#Target and features
X = student_performance_factors_for_model.drop(columns=['Exam_Score'])
y = student_performance_factors_for_model['Exam_Score']

#Training and tests variables
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=TEST_SIZE,
    random_state=RANDOM_STATE
)

#----------------------------------------------------------