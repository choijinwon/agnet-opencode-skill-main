from __future__ import annotations

import sys
import io
import os
import json
import joblib
import mlflow
import logging
from pathlib import Path


logging.getLogger("mlflow").setLevel(logging.ERROR)

AI_STUDIO_DIR = Path(__file__).resolve().parent
PROJECT_DIR = AI_STUDIO_DIR.parent

# AIU Studio template: prepare_selected_model.py rewrites these values for the selected model.
SOURCE_MODEL_PATH = PROJECT_DIR / "data" / "model.joblib"
DATA_MODEL_PATH = SOURCE_MODEL_PATH
MODEL_PATH = SOURCE_MODEL_PATH
MODEL_KIND = "unknown"
INPUT_EXAMPLE_PATH = AI_STUDIO_DIR / "input_example.json"

# MLflow/AI Studio settings
# User input: tracking URL, username, password.
# Auto values are rewritten from the selected model name.
mlflow_tracking_url = ""
mlflow_tracking_username = ""
mlflow_tracking_password = ""
mlflow_experiment_name = "aiu_studio"
mlflow_register_model_name = "aiu_studio_model"

# Remote deployment keeps mlflow_tracking_url empty until the user fills it in.
effective_mlflow_tracking_uri = mlflow_tracking_url


def load_selected_model():
    raise ValueError(f"unsupported MODEL_KIND: {MODEL_KIND}")


def main():
    model = load_selected_model()
    print(
        {
            "status": "loaded",
            "model_kind": MODEL_KIND,
            "model_path": str(MODEL_PATH),
            "model_type": type(model).__name__,
        }
    )


if __name__ == "__main__":
    main()
