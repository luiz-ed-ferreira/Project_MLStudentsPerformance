#Call libraries
import pandas as pd
from sklearn.model_selection import train_test_split

# Transformed dataset (from EDA)
#Students performance factors for model dataset
student_performance_factors_for_model = pd.read_csv('../Dataset/student_performance_factors_for_model.csv')

#Target and features
X = student_performance_factors_for_model.drop(columns=['Exam_Score'])
y = student_performance_factors_for_model['Exam_Score']

#Training and tests variables
#Considering (for a good performance):
    #80% -> Training
    #20% -> Test
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
#Summary: random_state=42 does not improve the model. It merely ensures that the randomness is reproducible.
#For other definitions 42 is "life, the universe, and everything else