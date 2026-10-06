"""
AgroPredict - Machine Learning Training Pipeline
Model: Random Forest Classifier
Dataset: Crop_recommendation.csv

This script trains a Random Forest Classifier to recommend optimal crops
based on seven agricultural and climatic parameters:
- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature (temperature)
- Relative Humidity (humidity)
- Soil pH (ph)
- Rainfall (rainfall)
"""

import os
import sys
import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Path configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(BASE_DIR, "Crop_recommendation.csv")
MODEL_SAVE_PATH = os.path.join(BASE_DIR, "crop_prediction_model.pkl")

# Expected feature columns in specific order
FEATURE_COLUMNS = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
TARGET_COLUMN = 'label'


def load_dataset(filepath: str) -> pd.DataFrame:
    """
    Loads and validates the Crop recommendation dataset.
    
    Args:
        filepath (str): Path to Crop_recommendation.csv
        
    Returns:
        pd.DataFrame: Loaded dataset
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Dataset not found at: {filepath}")
    
    print(f"[1/5] Loading dataset from: {filepath}")
    df = pd.read_csv(filepath)
    print(f"      Successfully loaded {df.shape[0]} rows and {df.shape[1]} columns.")
    
    # Verify required columns exist
    missing_cols = [col for col in FEATURE_COLUMNS + [TARGET_COLUMN] if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Dataset is missing required columns: {missing_cols}")
    
    # Check for missing/null values
    null_counts = df[FEATURE_COLUMNS + [TARGET_COLUMN]].isnull().sum().sum()
    if null_counts > 0:
        print(f"      Warning: Found {null_counts} null values. Dropping missing rows.")
        df = df.dropna(subset=FEATURE_COLUMNS + [TARGET_COLUMN])
    else:
        print("      Data integrity verified: 0 missing or null values.")

    unique_crops = df[TARGET_COLUMN].nunique()
    print(f"      Identified {unique_crops} unique crop classes.")
    return df


def prepare_data(df: pd.DataFrame, test_size: float = 0.2, random_state: int = 42):
    """
    Splits dataset into features and target, and creates stratified train/test splits.
    
    Args:
        df (pd.DataFrame): Input dataframe
        test_size (float): Proportion of dataset to include in test split
        random_state (int): Seed for reproducibility
        
    Returns:
        tuple: X_train, X_test, y_train, y_test
    """
    print(f"[2/5] Preparing data & splitting into train/test sets (test_size={test_size})...")
    X = df[FEATURE_COLUMNS]
    y = df[TARGET_COLUMN]
    
    # Use stratified split so all 22 crops are proportionally represented
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=test_size,
        random_state=random_state,
        stratify=y
    )
    
    print(f"      Training samples: {len(X_train)}")
    print(f"      Testing samples:  {len(X_test)}")
    return X_train, X_test, y_train, y_test


def train_model(X_train: pd.DataFrame, y_train: pd.Series, random_state: int = 42) -> RandomForestClassifier:
    """
    Initializes and fits a Random Forest Classifier.
    
    Args:
        X_train (pd.DataFrame): Training feature matrix
        y_train (pd.Series): Training labels
        random_state (int): Seed for reproducibility
        
    Returns:
        RandomForestClassifier: Trained model
    """
    print("[3/5] Training Random Forest Classifier...")
    model = RandomForestClassifier(
        n_estimators=100,
        criterion='gini',
        max_depth=None,
        min_samples_split=2,
        min_samples_leaf=1,
        random_state=random_state,
        n_jobs=-1
    )
    model.fit(X_train, y_train)
    print("      Model training complete.")
    return model


def evaluate_model(model: RandomForestClassifier, X_train: pd.DataFrame, y_train: pd.Series,
                   X_test: pd.DataFrame, y_test: pd.Series):
    """
    Calculates and displays model accuracy and evaluation metrics.
    
    Args:
        model: Trained classifier
        X_train: Training features
        y_train: Training labels
        X_test: Testing features
        y_test: Testing labels
    """
    print("[4/5] Evaluating model performance...")
    
    # Training accuracy
    y_train_pred = model.predict(X_train)
    train_acc = accuracy_score(y_train, y_train_pred)
    
    # Testing accuracy
    y_test_pred = model.predict(X_test)
    test_acc = accuracy_score(y_test, y_test_pred)
    
    print("\n" + "=" * 50)
    print("         AGROPREDICT MODEL PERFORMANCE")
    print("=" * 50)
    print(f" Training Accuracy: {train_acc * 100:.2f}%")
    print(f" Test Accuracy:     {test_acc * 100:.2f}%")
    print("=" * 50)
    
    print("\nDetailed Classification Report on Test Set:")
    print(classification_report(y_test, y_test_pred, digits=4))
    
    # Feature importances
    importances = model.feature_importances_
    print("Feature Importances:")
    for feature, imp in sorted(zip(FEATURE_COLUMNS, importances), key=lambda x: x[1], reverse=True):
        print(f" - {feature:<12}: {imp * 100:.2f}%")
        
    return test_acc


def save_model(model: RandomForestClassifier, filepath: str):
    """
    Serializes and saves the trained model to disk as a .pkl file.
    
    Args:
        model: Trained model
        filepath (str): Destination path
    """
    print(f"\n[5/5] Saving trained model to: {filepath}")
    
    # Save the model object directly so it can be loaded with standard pickle or joblib
    with open(filepath, 'wb') as f:
        pickle.dump(model, f)
        
    file_size_kb = os.path.getsize(filepath) / 1024
    print(f"      Model saved successfully! ({file_size_kb:.2f} KB)")


def main():
    """Main execution entry point."""
    print("==================================================")
    print("   AGROPREDICT - CROP RECOMMENDATION SYSTEM       ")
    print("   Model Training Pipeline                        ")
    print("==================================================\n")
    
    try:
        df = load_dataset(DATASET_PATH)
        X_train, X_test, y_train, y_test = prepare_data(df)
        model = train_model(X_train, y_train)
        evaluate_model(model, X_train, y_train, X_test, y_test)
        save_model(model, MODEL_SAVE_PATH)
        print("\nAll training steps completed successfully!")
    except Exception as e:
        print(f"\n[ERROR] An error occurred during training: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
