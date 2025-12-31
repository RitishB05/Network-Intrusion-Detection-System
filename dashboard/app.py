from flask import Flask, render_template, request
import sys
import os
import joblib
import pandas as pd
import logging
import numpy as np
import time

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Define paths to artifacts and data
try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    ARTIFACTS_DIR = os.path.join(BASE_DIR, '..', 'models')
    DATA_DIR = os.path.join(BASE_DIR, '..', 'data')
    MODEL_PATH = os.path.join(ARTIFACTS_DIR, 'binary_model.pkl')
    SCALER_PATH = os.path.join(ARTIFACTS_DIR, 'scaler.pkl')
    ENCODERS_PATH = os.path.join(ARTIFACTS_DIR, 'label_encoders.pkl')
    SELECTOR_PATH = os.path.join(ARTIFACTS_DIR, 'selector.pkl')
    TEST_DATA_PATH = os.path.join(DATA_DIR, 'UNSW_NB15_testing-set.csv')
    logger.info("Paths defined successfully.")
except Exception as e:
    logger.error(f"Error defining paths: {e}")
    sys.exit(1)

# Define training columns
training_columns = ['dur', 'proto', 'service', 'sbytes', 'dbytes']

# Check if required files exist
required_paths = [MODEL_PATH, SCALER_PATH, ENCODERS_PATH, SELECTOR_PATH]
for path in required_paths:
    if not os.path.exists(path):
        logger.error(f"Missing required file: {path}")
        sys.exit(1)

# Load preprocessing artifacts and model
try:
    scaler = joblib.load(SCALER_PATH)
    label_encoders = joblib.load(ENCODERS_PATH)
    selector = joblib.load(SELECTOR_PATH)
    model = joblib.load(MODEL_PATH)
    logger.info("All artifacts loaded successfully.")
except Exception as e:
    logger.error(f"Error loading artifacts: {e}")
    sys.exit(1)

def preprocess_data(df, ref_columns=None, scaler=None, label_encoders=None):
    """Preprocess input data for prediction."""
    try:
        logger.info(f"Input data shape: {df.shape}")
        logger.info(f"Input data columns: {list(df.columns)}")
        
        # Drop 'label' if present
        if 'label' in df.columns:
            y = df['label'].values
            df_copy = df.drop('label', axis=1)
        else:
            y = None
            df_copy = df.copy()
        
        # Align with ref_columns
        if ref_columns:
            df_copy = df_copy[ref_columns]
        
        X = df_copy.copy()
        logger.info(f"Data after aligning columns: {X.head()}")
        
        # Define categorical and numerical columns
        categorical_cols = ['proto', 'service']
        numerical_cols = ['dur', 'sbytes', 'dbytes']
        
        # Encode categorical columns
        for col in categorical_cols:
            if col in X.columns and col in label_encoders:
                le = label_encoders[col]
                logger.info(f"Unique values in {col} before encoding: {X[col].unique()}")
                unseen = set(X[col]) - set(le.classes_)
                if unseen:
                    logger.warning(f"Unseen categories in {col}: {unseen}")
                X[col] = X[col].apply(lambda x: x if x in le.classes_ else le.classes_[0])
                X[col] = le.transform(X[col])
                logger.info(f"Encoded values in {col}: {X[col].unique()}")
            elif col in X.columns:
                logger.warning(f"No encoder found for {col}, setting to 0")
                X[col] = 0
        
        # Scale numerical columns
        if scaler:
            logger.info(f"Scaling numerical columns: {numerical_cols}")
            X[numerical_cols] = scaler.transform(X[numerical_cols])
        
        # Ensure all columns are numerical
        X_scaled = X.values
        logger.info(f"Preprocessed data shape: {X_scaled.shape}")
        return X_scaled, y, None, None, None
    except Exception as e:
        logger.error(f"Preprocessing error: {e}")
        raise

@app.route('/')
def index():
    """Render the main page with input form."""
    try:
        logger.info("Rendering index.html")
        return render_template('index.html')
    except Exception as e:
        logger.error(f"Error rendering index.html: {e}")
        return "Error: Unable to render index.html. Please check the logs and ensure the template exists in the templates/ directory.", 500

@app.route("/classify", methods=["POST"])
def classify():
    """Handle manual classification from form input."""
    try:
        dur = float(request.form["dur"])
        proto = request.form["proto"]
        service = request.form["service"]
        sbytes = int(request.form["sbytes"])
        dbytes = int(request.form["dbytes"])
        input_data = pd.DataFrame([[dur, proto, service, sbytes, dbytes]], columns=training_columns)
        logger.info(f"Input data: {input_data}")
        
        X_scaled, _, _, _, _ = preprocess_data(input_data, ref_columns=training_columns, scaler=scaler, label_encoders=label_encoders)
        X_red = selector.transform(X_scaled)
        logger.info(f"Shape after selector: {X_red.shape}")
        
        prediction = model.predict(X_red)[0]
        result = "Attack" if prediction == 1 else "Normal"
        logger.info(f"Prediction: {result}")
        
        return render_template("result.html", result=result)
    except Exception as e:
        logger.error(f"Classification error: {e}")
        try:
            return render_template("result.html", result=f"Error: {str(e)}")
        except Exception as template_error:
            logger.error(f"Error rendering result.html: {template_error}")
            return "Error: Unable to render result.html. Please check the logs and ensure the template exists in the templates/ directory.", 500

@app.route("/simulate")
def simulate():
    """Simulate real-time predictions using test data."""
    try:
        if not os.path.exists(TEST_DATA_PATH):
            logger.warning(f"Test data not found at {TEST_DATA_PATH}. Simulation unavailable.")
            try:
                return render_template("result.html", result="Error: Test data file (UNSW_NB15_testing-set.csv) not found. Please add it to the data/ directory.")
            except Exception as template_error:
                logger.error(f"Error rendering result.html: {template_error}")
                return "Error: Unable to render result.html. Please check the logs and ensure the template exists in the templates/ directory.", 500
        
        # Start timing the simulation
        start_time = time.time()
        
        # Load the entire test dataset and randomly sample 100 rows
        test_df = pd.read_csv(TEST_DATA_PATH)
        logger.info(f"Test data loaded: {test_df.shape}")
        test_df = test_df.sample(n=100, random_state=None)  # Randomly select 100 rows
        logger.info(f"Sampled data: {test_df.shape}")
        
        if 'label' in test_df.columns:
            test_df = test_df.drop('label', axis=1)
        test_df = test_df[training_columns]
        
        # Preprocess the data
        X_test, _, _, _, _ = preprocess_data(
            test_df,
            ref_columns=training_columns,
            scaler=scaler,
            label_encoders=label_encoders
        )
        
        # Apply VarianceThreshold selector
        X_test_red = selector.transform(X_test)
        logger.info(f"Shape after selector: {X_test_red.shape}")
        
        # Make predictions and get probabilities
        predictions = model.predict(X_test_red)
        prediction_labels = ["Attack" if p == 1 else "Normal" for p in predictions]
        
        # Check if the model supports predict_proba
        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(X_test_red)
            # Probability of being an Attack (class 1)
            attack_probs = probabilities[:, 1] * 100  # Convert to percentage
            normal_probs = probabilities[:, 0] * 100  # Probability of being Normal
        else:
            # Fallback if predict_proba is not available
            attack_probs = [100 if p == "Attack" else 0 for p in prediction_labels]
            normal_probs = [100 if p == "Normal" else 0 for p in prediction_labels]
            logger.warning("Model does not support predict_proba. Using binary probabilities.")
        
        logger.info(f"Predictions made: {len(prediction_labels)}")
        
        # Calculate runtime
        runtime = time.time() - start_time
        logger.info(f"Simulation runtime: {runtime:.2f} seconds")
        
        # Get input data for display
        input_data = test_df.to_dict(orient='records')
        
        # Combine input data, predictions, and probabilities
        results = [
            {
                "dur": data["dur"],
                "proto": data["proto"],
                "service": data["service"],
                "sbytes": data["sbytes"],
                "dbytes": data["dbytes"],
                "prediction": pred,
                "attack_prob": f"{prob_attack:.2f}%",
                "normal_prob": f"{prob_normal:.2f}%"
            }
            for data, pred, prob_attack, prob_normal in zip(input_data, prediction_labels, attack_probs, normal_probs)
        ]
        
        # Render the simulation template with results and runtime
        return render_template("simulate.html", results=results, runtime=f"{runtime:.2f}")
    except Exception as e:
        logger.error(f"Simulation error: {e}")
        try:
            return render_template("result.html", result=f"Error: {str(e)}")
        except Exception as template_error:
            logger.error(f"Error rendering result.html: {template_error}")
            return "Error: Unable to render result.html. Please check the logs and ensure the template exists in the templates/ directory.", 500

if __name__ == "__main__":
    # Run with debug mode to get detailed error tracebacks
    try:
        logger.info("Starting Flask app...")
        app.run(host='127.0.0.1', port=5000, debug=True)
    except Exception as e:
        logger.error(f"Error starting Flask app: {e}")
        sys.exit(1)
        
