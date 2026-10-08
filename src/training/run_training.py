#Call libraries
from src.config import (
BASELINE_METRICS_FILENAME,
    BASELINE_MODEL_FILENAME,
    DATASET_FILENAME,
)
from src.training.artifacts import save_metrics, save_model
from src.training.data_loader import load_dataset
from src.training.evaluation import evaluate_regression
from src.training.train import train_baseline

#----------------------------------------------------------

#Baseline training workflow
def run_baseline_training() -> None:
    """Execute the complete baseline training workflow. """

    dataframe = load_dataset(DATASET_FILENAME)

    model, X_test, y_test = train_baseline(dataframe)

    metrics = evaluate_regression(model, X_test, y_test)

    model_path = save_model(
        model,
        BASELINE_MODEL_FILENAME,
    )

    metrics_path = save_metrics(
        metrics,
        BASELINE_METRICS_FILENAME,
    )

    print("Baseline training completed successfully.")

    for metric_name, value in metrics.items():
        print(f"{metric_name}: {value:.4f}")

    print(f"Model saved to: {model_path}")
    print(f"Metrics saved to: {metrics_path}")

#----------------------------------------------------------

#Main entrypoint for the script
if __name__ == "__main__":
    run_baseline_training()

#----------------------------------------------------------