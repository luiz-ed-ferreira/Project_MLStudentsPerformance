#Call libraries
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

#----------------------------------------------------------

#Fucntion to evaluate a regression model using common performance metrics
def evaluate_regression(model, X_test: pd.DataFrame, y_test: pd.Series) -> dict[str, float]:
    """ Evaluate a regression model using common performance metrics. """

    #Generate predictions using the test dataset
    predictions = model.predict(X_test)

    #Calculate the main regression metrics
    mae = mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(
        mean_squared_error(y_test, predictions)
    )
    r2 = r2_score(y_test, predictions)

    #Calculate adjusted R-squared.
    n = len(y_test)
    p = model.named_steps["preprocessor"].transform(
        X_test
    ).shape[1]

    adjusted_r2 = (
        1 - (1 - r2) * (n - 1) / (n - p - 1)
        if n > p + 1
        else float("nan")
    )

    return {
        "MAE": float(mae),
        "RMSE": float(rmse),
        "R2": float(r2),
        "Adjusted_R2": float(adjusted_r2),
    }