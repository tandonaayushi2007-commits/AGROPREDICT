# AgroPredict 🌾

**AgroPredict** is an intelligent Agriculture Crop Recommendation System built using Machine Learning and Python Flask. It assists farmers, agronomists, and agricultural researchers in determining the most suitable crop to cultivate based on seven soil nutritional and climatic indicators:

- **Nitrogen (N)**
- **Phosphorus (P)**
- **Potassium (K)**
- **Temperature (°C)**
- **Relative Humidity (%)**
- **Soil pH (0 - 14)**
- **Rainfall (mm)**

---

## 🌟 Features

- **High-Accuracy Machine Learning Model**: Random Forest Classifier trained on 2,200 authentic field records, achieving **99.55% test accuracy** across 22 crops.
- **Full REST API**: Clean `POST /predict` API with comprehensive dual-layer validation for realistic agronomic boundaries.
- **22 Supported Agricultural Crops**: Complete with deep agronomic profiles (soil types, water needs, growth cycles, practical cultivation tips, and market values).
- **Modern Agriculture-Themed UI**: Responsive dashboard styled with organic emerald and warm earthy tones.
- **Quick-Test Presets**: One-click preset buttons for Rice, Coffee, Cotton, Apple, and Watermelon for rapid demonstrations.
- **Prediction History (localStorage)**: Saves past recommendations directly in your browser with parameter breakdowns and a 1-click **Load into Form** feature.
- **Dual Validation & Error Reporting**: Real-time inline field feedback and server-side validation messages.

---

## 📁 Project Structure

```text
AgroPredict/
│
├── Crop_recommendation.csv    # Authentic dataset (2,200 rows, 22 crops)
├── train.py                   # Machine learning training script
├── crop_prediction_model.pkl  # Trained Random Forest model artifact
├── crop_data.py               # Agronomic knowledge base for all 22 crops
├── app.py                     # Flask web server and POST /predict REST API
├── test_app.py                # Automated unit and integration test suite
├── requirements.txt           # Python package dependencies
│
├── templates/
│   └── index.html             # Modern responsive web template
│
└── static/
    ├── css/
    │   └── style.css          # Agriculture-themed stylesheet
    └── js/
        └── app.js             # Form validation, AJAX requests, localStorage history
```

---

## ⚙️ Prerequisites

- **Python 3.8+** (Python 3.10, 3.11, 3.12, 3.13 supported)
- **Windows Command Prompt (cmd)** or **PowerShell**

---

## 🚀 How to Run the Project on Windows

### Step 1: Open Terminal and Navigate to Project Directory

Open **PowerShell** or **Command Prompt** and switch to the project directory:

```powershell
cd C:\Users\Admin\.gemini\antigravity\scratch\AgroPredict
```

---

### Step 2: (Optional but Recommended) Create a Virtual Environment

```powershell
python -m venv venv
.\venv\Scripts\activate
```

---

### Step 3: Install Required Dependencies

```powershell
pip install -r requirements.txt
```

*Required packages include:*
- `Flask`
- `pandas`
- `numpy`
- `scikit-learn`

---

### Step 4: Train the Machine Learning Model

Run the training pipeline:

```powershell
python train.py
```

**Expected output:**
```text
==================================================
   AGROPREDICT - CROP RECOMMENDATION SYSTEM       
   Model Training Pipeline                        
==================================================
[1/5] Loading dataset from: ...\Crop_recommendation.csv
      Successfully loaded 2200 rows and 8 columns.
[2/5] Preparing data & splitting into train/test sets (test_size=0.2)...
[3/5] Training Random Forest Classifier...
[4/5] Evaluating model performance...
 Training Accuracy: 100.00%
 Test Accuracy:     99.55%
[5/5] Saving trained model to: ...\crop_prediction_model.pkl
All training steps completed successfully!
```

---

### Step 5: Start the Flask Web Application

```powershell
python app.py
```

**Expected terminal output:**
```text
============================================================
  AGROPREDICT - Crop Recommendation System Web Server
  Running locally on http://127.0.0.1:5000
============================================================
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

---

### Step 6: Open the Application in Your Browser

Open any web browser (Chrome, Edge, Firefox) and navigate to:

👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 🧪 Running the Automated Tests

To run the automated test suite verifying endpoints, validation, and model inference:

```powershell
python test_app.py
```

All 9 tests will execute and report `OK`.

---

## 📡 REST API Reference

### `POST /predict`

Recommends the best crop for given soil and environmental conditions.

**Request Body (`application/json`):**
```json
{
  "N": 90,
  "P": 42,
  "K": 43,
  "temperature": 21.5,
  "humidity": 82.0,
  "ph": 6.5,
  "rainfall": 202.9
}
```

**Response (`200 OK`):**
```json
{
  "status": "success",
  "predicted_crop": "rice",
  "display_name": "Rice",
  "icon": "🌾",
  "confidence": 99.5,
  "crop_info": {
    "name": "Rice",
    "scientific_name": "Oryza sativa",
    "category": "Cereal Grain / Staple Food",
    "ideal_temp": "20°C - 35°C",
    "ideal_rainfall": "150 - 300 mm",
    "soil_type": "Clayey loam, alluvial soil with good water retention",
    "water_requirement": "Very High",
    "growing_season": "Kharif (Monsoon) / Summer",
    "duration": "100 - 150 days",
    "farming_tips": [ ... ],
    "economic_value": "..."
  },
  "top_candidates": [
    { "crop": "rice", "display_name": "Rice", "probability": 99.5, "icon": "🌾" },
    { "crop": "jute", "display_name": "Jute", "probability": 0.5, "icon": "🧶" }
  ]
}
```

---

## 🌿 Supported Crops (22 Total)

- **Cereals & Grains**: Rice, Maize
- **Pulses & Legumes**: Chickpea, Kidney Beans, Pigeon Peas, Moth Beans, Mung Bean, Black Gram, Lentil
- **Fruits**: Banana, Mango, Grapes, Apple, Orange, Papaya, Pomegranate, Watermelon, Muskmelon
- **Plantation & Cash Crops**: Coconut, Cotton, Jute, Coffee

---

## 👥 Developers

- **Aayushi Tandon** (72511209)
- **Amritpal** (72512012)
