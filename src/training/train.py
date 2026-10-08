#Call libraries
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from src.config import RANDOM_STATE, TEST_SIZE
from src.training.data_loader import split_features_target

#----------------------------------------------------------

#Function to train a baseline Linear Regression model and return the fitted pipeline and test data
def train_baseline(dataframe: pd.DataFrame,) -> tuple[Pipeline, pd.DataFrame, pd.Series]:
    """ Train a baseline Linear Regression model and return the fitted pipeline and test data. """

    #Remove rows containing missing values
    dataframe = dataframe.dropna().copy()

    #Separate input features from the target variable
    X, y = split_features_target(dataframe)

    #Identify categorical features
    categorical_columns = X.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()

    #Configure categorical feature encoding
    preprocessor = ColumnTransformer(
        transformers=[
            (
                "categorical",
                OneHotEncoder(
                    handle_unknown="ignore",
                    sparse_output=False,
                ),
                categorical_columns,
            )
        ],
        remainder="passthrough",
    )

    #Build the complete Machine Learning pipeline
    model_pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("regressor", LinearRegression()),
        ]
    )

    #Split the dataset into training and testing subsets
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
    )

    #Fit the preprocessing and regression model
    model_pipeline.fit(X_train, y_train)

    return model_pipeline, X_test, y_test