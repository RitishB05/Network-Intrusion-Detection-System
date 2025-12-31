import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARTIFACTS_DIR = os.path.join(BASE_DIR, '..', 'models')
MODEL_PATH = os.path.join(ARTIFACTS_DIR, 'binary_model.pkl')
SCALER_PATH = os.path.join(ARTIFACTS_DIR, 'scaler.pkl')
ENCODERS_PATH = os.path.join(ARTIFACTS_DIR, 'label_encoders.pkl')
SELECTOR_PATH = os.path.join(ARTIFACTS_DIR, 'selector.pkl')

print("Loading artifacts...")
scaler = joblib.load(SCALER_PATH)
label_encoders = joblib.load(ENCODERS_PATH)
selector = joblib.load(SELECTOR_PATH)
model = joblib.load(MODEL_PATH)
print("All artifacts loaded successfully.")