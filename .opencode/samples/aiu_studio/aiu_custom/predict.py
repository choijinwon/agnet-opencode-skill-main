from __future__ import annotations

from pathlib import Path


AIU_CUSTOM_DIR = Path(__file__).resolve().parent
AI_STUDIO_DIR = AIU_CUSTOM_DIR.parent
PROJECT_DIR = AI_STUDIO_DIR.parent

# AIU Studio template: prepare_selected_model.py rewrites these values for the selected model.
SOURCE_MODEL_PATH = PROJECT_DIR / "data" / "model.joblib"
DATA_MODEL_PATH = SOURCE_MODEL_PATH
MODEL_PATH = SOURCE_MODEL_PATH
MODEL_KIND = "unknown"


def load_selected_model():
    raise ValueError(f"unsupported MODEL_KIND: {MODEL_KIND}")


class ModelWrapper:
    def __init__(self):
        self.model = None

    def load_context(self, context=None):
        if self.model is None:
            self.model = load_selected_model()
        return self.model

    def predict(self, context, model_input):
        model = self.load_context(context)
        if hasattr(model, "predict"):
            return model.predict(model_input)
        if callable(model):
            return model(model_input)
        return {
            "status": "loaded",
            "model_kind": MODEL_KIND,
            "model_path": str(MODEL_PATH),
            "input": model_input,
        }


def predict(payload):
    return ModelWrapper().predict(None, payload)
