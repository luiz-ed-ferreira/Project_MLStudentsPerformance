#Call libraries
from pathlib import Path
import pandas as pd
from src.config import DATA_DIR, TARGET

#----------------------------------------------------------

def load_dataset(filename: str) -> pd.DataFrame:
    """ Load a dataset from the configured data directory. """
    file_path = DATA_DIR / filename

    if not file_path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {file_path}"
        )

    return pd.read_csv(file_path)

#----------------------------------------------------------

def split_features_target(dataframe: pd.DataFrame,) -> tuple[pd.DataFrame, pd.Series]:
    """ Separate input features from the target variable. """
    if TARGET not in dataframe.columns:
        raise ValueError(
            f"Target column '{TARGET}' not found."
        )

    X = dataframe.drop(columns=[TARGET])
    y = dataframe[TARGET]

    return X, y

#----------------------------------------------------------
