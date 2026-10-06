"""
AgroPredict - Flask Backend Web Application & REST API
Provides endpoints for crop prediction, input validation, and crop knowledge delivery.
"""

import os
import sys
import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template

from crop_data import get_crop_info, CROP_DATABASE

# Base directories & paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "crop_prediction_model.pkl")
DATASET_PATH = os.path.join(BASE_DIR, "Crop_recommendation.csv")

# Initialize Flask application with explicit absolute paths for Linux/Render compatibility
app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

# Expected features in the exact training order
FEATURE_ORDER = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']

# Validation boundaries for agricultural and physical realism
FIELD_VALIDATION_RULES = {
    'N': {
        'label': 'Nitrogen (N)',
        'min': 0.0,
        'max': 300.0,
        'unit': 'kg/ha',
        'type': 'numeric'
    },
    'P': {
        'label': 'Phosphorus (P)',
        'min': 0.0,
        'max': 300.0,
        'unit': 'kg/ha',
        'type': 'numeric'
    },
    'K': {
        'label': 'Potassium (K)',
        'min': 0.0,
        'max': 350.0,
        'unit': 'kg/ha',
        'type': 'numeric'
    },
    'temperature': {
        'label': 'Temperature',
        'min': -5.0,
        'max': 60.0,
        'unit': '°C',
        'type': 'numeric'
    },
    'humidity': {
        'label': 'Relative Humidity',
        'min': 0.0,
        'max': 100.0,
        'unit': '%',
        'type': 'numeric'
    },
    'ph': {
        'label': 'Soil pH',
        'min': 0.0,
        'max': 14.0,
        'unit': 'pH scale',
        'type': 'numeric'
    },
    'rainfall': {
        'label': 'Rainfall',
        'min': 0.0,
        'max': 1500.0,
        'unit': 'mm',
        'type': 'numeric'
    }
}

# Global model variable
model = None


def load_trained_model():
    """
    Loads the trained Random Forest model from disk.
    If the model does not exist yet, attempts to train it from Crop_recommendation.csv,
    or raises a clear error.
    """
    global model
    if not os.path.exists(MODEL_PATH):
        print(f"[AgroPredict] Trained model not found at {MODEL_PATH}. Checking for dataset at {DATASET_PATH}...")
        if os.path.exists(DATASET_PATH):
            try:
                from train import main as run_train
                print("[AgroPredict] Model artifact missing. Automatically training Random Forest model...")
                run_train()
            except Exception as e:
                raise FileNotFoundError(
                    f"Model not found and automated training failed: {e}. "
                    "Please run 'python train.py' to generate crop_prediction_model.pkl."
                )
        else:
            raise FileNotFoundError(
                f"Trained model not found at {MODEL_PATH} and dataset missing at {DATASET_PATH}. "
                "Please run 'python train.py' first to train and serialize the model."
            )

    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    print(f"[AgroPredict] Model successfully loaded from: {MODEL_PATH}")


# Load model at application startup
try:
    load_trained_model()
except Exception as err:
    print(f"[AgroPredict Startup Warning] Could not load model: {err}", file=sys.stderr)


# ============================================================================
# Web Routes
# ============================================================================

@app.route('/', methods=['GET'])
def index():
    """Renders the main AgroPredict web interface."""
    return render_template('index.html')


@app.route('/health', methods=['GET'])
def health():
    """Healthcheck endpoint for monitoring application status."""
    return jsonify({
        "status": "healthy",
        "model_loaded": model is not None,
        "features": FEATURE_ORDER,
        "crops_supported": len(CROP_DATABASE)
    }), 200


@app.route('/api/presets', methods=['GET'])
def get_presets():
    """Returns realistic sample presets for convenient testing."""
    presets = [
        {
            "name": "High-Rainfall Paddy (Rice)",
            "description": "Warm, humid conditions with high water availability and balanced nitrogen.",
            "data": {"N": 90, "P": 42, "K": 43, "temperature": 21.5, "humidity": 82.0, "ph": 6.5, "rainfall": 210.0}
        },
        {
            "name": "High-Altitude Plantation (Coffee)",
            "description": "Moderate temperatures, rich potassium, and gentle tropical showers.",
            "data": {"N": 101, "P": 29, "K": 32, "temperature": 26.5, "humidity": 58.0, "ph": 6.8, "rainfall": 160.0}
        },
        {
            "name": "Semi-Arid Black Soil (Cotton)",
            "description": "High temperature, sunny skies, moderate humidity, and balanced phosphorus.",
            "data": {"N": 118, "P": 47, "K": 20, "temperature": 24.0, "humidity": 80.0, "ph": 6.9, "rainfall": 80.0}
        },
        {
            "name": "Temperate Mountain Valley (Apple)",
            "description": "Cooler climate, high potassium/phosphorus, and high relative humidity.",
            "data": {"N": 24, "P": 134, "K": 198, "temperature": 22.0, "humidity": 92.5, "ph": 6.1, "rainfall": 110.0}
        },
        {
            "name": "Dry Sandy Riverbed (Watermelon)",
            "description": "Warm sunny days, low nitrogen, high potassium, and moderate rainfall.",
            "data": {"N": 99, "P": 18, "K": 51, "temperature": 25.5, "humidity": 88.0, "ph": 6.5, "rainfall": 50.0}
        }
    ]
    return jsonify({"status": "success", "presets": presets}), 200


@app.route('/api/crops', methods=['GET'])
def get_crops():
    """Returns full catalog of all 22 supported crops and their metadata."""
    return jsonify({
        "status": "success",
        "total_crops": len(CROP_DATABASE),
        "crops": CROP_DATABASE
    }), 200


@app.route('/predict', methods=['POST'])
def predict():
    """
    POST API endpoint for crop prediction.
    Accepts JSON payload containing N, P, K, temperature, humidity, ph, rainfall.
    Performs validation and runs real inference through the trained Random Forest model.
    """
    global model
    if model is None:
        try:
            load_trained_model()
        except Exception as e:
            return jsonify({
                "status": "error",
                "message": f"Machine learning model is not available. Please ensure model is trained: {str(e)}"
            }), 500

    # Extract request payload (support JSON and form data)
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form.to_dict()

    if not data:
        return jsonify({
            "status": "error",
            "message": "Empty request. Please provide JSON or form body with required parameters."
        }), 400

    # -------------------------------------------------------------------------
    # Validation: Check presence, type, and realistic boundaries
    # -------------------------------------------------------------------------
    errors = {}
    cleaned_inputs = {}

    for field in FEATURE_ORDER:
        rule = FIELD_VALIDATION_RULES[field]
        label = rule['label']
        min_val = rule['min']
        max_val = rule['max']
        unit = rule['unit']

        if field not in data:
            errors[field] = f"Field '{label}' ({field}) is missing from request."
            continue

        raw_val = data[field]
        if raw_val is None or str(raw_val).strip() == "":
            errors[field] = f"Please enter a value for {label}."
            continue

        try:
            numeric_val = float(raw_val)
        except (ValueError, TypeError):
            errors[field] = f"{label} must be a valid number. Received: '{raw_val}'."
            continue

        # Check bounds
        if numeric_val < min_val or numeric_val > max_val:
            errors[field] = (
                f"{label} ({numeric_val} {unit}) is out of realistic range. "
                f"Expected between {min_val} and {max_val} {unit}."
            )
            continue

        cleaned_inputs[field] = numeric_val

    # Return descriptive validation errors if any failed
    if errors:
        return jsonify({
            "status": "error",
            "message": "Validation failed for one or more input parameters.",
            "errors": errors
        }), 400

    # -------------------------------------------------------------------------
    # Model Inference: Real prediction using trained Random Forest Classifier
    # -------------------------------------------------------------------------
    try:
        # Prepare input features DataFrame with proper column names
        feature_df = pd.DataFrame([cleaned_inputs], columns=FEATURE_ORDER)
        
        # Predict class label
        prediction = model.predict(feature_df)[0]
        
        # Predict class probabilities for confidence computation
        top_candidates = []
        confidence_percent = 95.0  # fallback if proba not available
        
        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(feature_df)[0]
            classes = model.classes_
            
            # Sort crops by probability descending
            ranked_indices = np.argsort(probabilities)[::-1]
            
            # Top predicted crop confidence
            top_idx = ranked_indices[0]
            confidence_percent = round(float(probabilities[top_idx] * 100), 2)
            
            # Top 3 candidates for insights
            for idx in ranked_indices[:3]:
                crop_name = classes[idx]
                info = get_crop_info(crop_name)
                top_candidates.append({
                    "crop": crop_name,
                    "display_name": info.get("name", crop_name.capitalize()),
                    "icon": info.get("icon", "🌱"),
                    "probability": round(float(probabilities[idx] * 100), 2)
                })

        # Fetch comprehensive agronomic data for predicted crop
        crop_details = get_crop_info(prediction)

        return jsonify({
            "status": "success",
            "predicted_crop": prediction,
            "display_name": crop_details.get("name", prediction.capitalize()),
            "icon": crop_details.get("icon", "🌱"),
            "confidence": confidence_percent,
            "crop_info": crop_details,
            "top_candidates": top_candidates,
            "inputs_received": cleaned_inputs
        }), 200

    except Exception as exc:
        return jsonify({
            "status": "error",
            "message": f"Inference execution failed: {str(exc)}"
        }), 500


# Application entry point
if __name__ == '__main__':
    # Render and cloud deployment configuration:
    # Listens on 0.0.0.0 and binds to the PORT environment variable assigned by Render.
    port = int(os.environ.get("PORT", 5000))
    host = os.environ.get("HOST", "0.0.0.0")
    debug_mode = os.environ.get("FLASK_DEBUG", "False").lower() in ("true", "1", "t")

    print("=" * 60)
    print("  AGROPREDICT - Crop Recommendation System Web Server")
    print(f"  Listening on http://{host}:{port}")
    print("=" * 60)
    app.run(host=host, port=port, debug=debug_mode)
