from src.training.data_loader import load_dataset
from src.training.train import train_baseline
from src.training.evaluation import evaluate_regression


def main() -> None:
    dataframe = load_dataset('../data/student_performance_factors_for_model.csv')

    model, X_test, y_test = train_baseline(dataframe)

    metrics = evaluate_regression(
        model,
        X_test,
        y_test,
    )

    print("Baseline Model Evaluation")

    for metric_name, value in metrics.items():
        print(f"{metric_name}: {value:.4f}")


if __name__ == "__main__":
    main()