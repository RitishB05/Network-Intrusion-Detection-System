# train_model.py
import joblib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, classification_report, f1_score, roc_auc_score, confusion_matrix
from imblearn.over_sampling import SMOTE
from sklearn.feature_selection import SelectKBest, f_classif, VarianceThreshold
from sklearn.pipeline import make_pipeline
from sklearn.calibration import CalibratedClassifierCV
from data_preprocessing import load_data, preprocess_data

def calculate_fpr_fnr(y_true, y_pred):
    """Calculate False Positive Rate and False Negative Rate"""
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    fpr = fp / (fp + tn) if (fp + tn) > 0 else 0
    fnr = fn / (fn + tp) if (fn + tp) > 0 else 0
    return fpr, fnr

def plot_feature_importance(model, feature_names, top_n=5, filename='feature_importance.pdf'):
    """
    Plot feature importance from a trained model.
    
    Args:
        model: Trained model with feature_importances_ attribute
        feature_names: List of feature names
        top_n: Number of top features to highlight
        filename: Output filename for the plot
    """
    # Get feature importances
    importances = model.feature_importances_
    
    # Sort features by importance
    sorted_idx = importances.argsort()
    
    # Determine top features for highlighting
    top_features = set(feature_names[sorted_idx][-top_n:])
    colors = ['#1f77b4' if feat in top_features else '#d3d3d3' for feat in feature_names[sorted_idx]]
    
    # Create plot
    plt.figure(figsize=(10, 6))
    sns.barplot(x=importances[sorted_idx], 
                y=np.array(feature_names)[sorted_idx], 
                palette=colors)
    plt.title('Feature Importance Ranking (Random Forest)')
    plt.xlabel('Gini Importance Score')
    plt.ylabel('Features')
    plt.tight_layout()
    plt.savefig(filename, bbox_inches='tight')
    plt.close()
    print(f"Feature importance plot saved to {filename}")

    def evaluate_runtime_performance(test_path, model_path="models/binary_model.pkl"):
    # Load test data
    _, test_df = load_data(None, test_path)
    test_df = test_df.drop('attack_cat', axis=1, errors='ignore')

    # Load preprocessing artifacts
    try:
        scaler = joblib.load("models/scaler.pkl")
        label_encoders = joblib.load("models/label_encoders.pkl")
        selector = joblib.load("models/selector.pkl")
        training_columns = joblib.load("models/training_columns.pkl")
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Missing artifact: {e}")def evaluate_runtime_performance(test_path, model_path="models/binary_model.pkl"):
    # Load test data
    _, test_df = load_data(None, test_path)
    test_df = test_df.drop('attack_cat', axis=1, errors='ignore')

    # Load preprocessing artifacts
    try:
        scaler = joblib.load("models/scaler.pkl")
        label_encoders = joblib.load("models/label_encoders.pkl")
        selector = joblib.load("models/selector.pkl")
        training_columns = joblib.load("models/training_columns.pkl")
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Missing artifact: {e}")

def train_and_evaluate(train_path, test_path):def evaluate_runtime_performance(test_path, model_path="models/binary_model.pkl"):
    # Load test data
    _, test_df = load_data(None, test_path)
    test_df = test_df.drop('attack_cat', axis=1, errors='ignore')

    # Load preprocessing artifacts
    try:
        scaler = joblib.load("models/scaler.pkl")
        label_encoders = joblib.load("models/label_encoders.pkl")
        selector = joblib.load("models/selector.pkl")
        training_columns = joblib.load("models/training_columns.pkl")
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Missing artifact: {e}")def evaluate_runtime_performance(test_path, model_path="models/binary_model.pkl"):
    # Load test data
    _, test_df = load_data(None, test_path)
    test_df = test_df.drop('attack_cat', axis=1, errors='ignore')

    # Load preprocessing artifacts
    try:
        scaler = joblib.load("models/scaler.pkl")
        label_encoders = joblib.load("models/label_encoders.pkl")
        selector = joblib.load("models/selector.pkl")
        training_columns = joblib.load("models/training_columns.pkl")
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Missing artifact: {e}")def evaluate_runtime_performance(test_path, model_path="models/binary_model.pkl"):
    # Load test data
    _, test_df = load_data(None, test_path)
    test_df = test_df.drop('attack_cat', axis=1, errors='ignore')

    # Load preprocessing artifacts
    try:
        scaler = joblib.load("models/scaler.pkl")
        label_encoders = joblib.load("models/label_encoders.pkl")
        selector = joblib.load("models/selector.pkl")
        training_columns = joblib.load("models/training_columns.pkl")
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Missing artifact: {e}")def evaluate_runtime_performance(test_path, model_path="models/binary_model.pkl"):
    # Load test data
    _, test_df = load_data(None, test_path)
    test_df = test_df.drop('attack_cat', axis=1, errors='ignore')

    # Load preprocessing artifacts
    try:
        scaler = joblib.load("models/scaler.pkl")
        label_encoders = joblib.load("models/label_encoders.pkl")
        selector = joblib.load("models/selector.pkl")
        training_columns = joblib.load("models/training_columns.pkl")
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Missing artifact: {e}")def evaluate_runtime_performance(test_path, model_path="models/binary_model.pkl"):
    # Load test data
    _, test_df = load_data(None, test_path)
    test_df = test_df.drop('attack_cat', axis=1, errors='ignore')

    # Load preprocessing artifacts
    try:
        scaler = joblib.load("models/scaler.pkl")
        label_encoders = joblib.load("models/label_encoders.pkl")
        selector = joblib.load("models/selector.pkl")
        training_columns = joblib.load("models/training_columns.pkl")
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Missing artifact: {e}")
    # Load and preprocess data
    train_df, test_df = load_data(train_path, test_path)
    train_df = train_df.drop('attack_cat', axis=1)
    test_df = test_df.drop('attack_cat', axis=1)

    # Load the training columns saved by data_preprocessing.py
    training_columns = joblib.load("models/training_columns.pkl")
    print("Training columns:", training_columns)

    # Ensure training_columns is a list of 5 features
    if not isinstance(training_columns, list) or len(training_columns) != 5:
        raise ValueError(f"Expected training_columns to be a list of 5 features, got {len(training_columns)}: {training_columns}")

    # Verify that all columns exist in train_df and test_df
    missing_columns_train = [col for col in training_columns + ['label'] if col not in train_df.columns]
    if missing_columns_train:
        raise ValueError(f"Missing columns in train_df: {missing_columns_train}")

    missing_columns_test = [col for col in training_columns + ['label'] if col not in test_df.columns]
    if missing_columns_test:
        raise ValueError(f"Missing columns in test_df: {missing_columns_test}")

    # Preprocess with the 5 features, ensuring a DataFrame
    X_train, y_train, ref_columns, scaler, label_encoders = preprocess_data(train_df[training_columns + ['label']].copy())
    X_test, y_test, _, _, _ = preprocess_data(test_df[training_columns + ['label']].copy(), ref_columns=training_columns, scaler=scaler, label_encoders=label_encoders)
    
    # Verify y_test is not None
    if y_test is None:
        raise ValueError("y_test is None; ensure 'label' column is present in test_df.")

    # Save preprocessing artifacts
    joblib.dump(scaler, "models/scaler.pkl")
    joblib.dump(label_encoders, "models/label_encoders.pkl")

    # Apply SMOTE to balanced data
    smote = SMOTE(random_state=42)
    X_train_bal, y_train_bal = smote.fit_resample(X_train, y_train)

    # Reduce memory usage by converting to float32
    X_train_bal = X_train_bal.astype(np.float32)
    X_test = X_test.astype(np.float32)

    # Remove constant features
    selector = VarianceThreshold()
    X_train_red = selector.fit_transform(X_train_bal)
    X_test_red = selector.transform(X_test)
    joblib.dump(selector, "models/selector.pkl")  # Save the selector for prediction

    # Check feature consistency
    print("X_train_red shape:", X_train_red.shape)
    print("X_test_red shape:", X_test_red.shape)

    # Define optimized models
    models = {
        "Logistic Regression (Balanced)": LogisticRegression(
            class_weight='balanced',
            max_iter=1000,
            solver='saga',
            penalty='l1',
            random_state=42
        ),
        "Random Forest (Optimized)": RandomForestClassifier(
            class_weight='balanced',
            max_depth=20,
            min_samples_split=5,
            n_estimators=100,
            max_features='sqrt',
            random_state=42
        ),
        "Linear SVM (Fast)": make_pipeline(
            SelectKBest(f_classif, k=5),  # Adjusted k to match number of features (5)
            LinearSVC(
                class_weight='balanced',
                dual=False,
                max_iter=1000,
                random_state=42
            )
        ),
        "HistGradientBoosting": HistGradientBoostingClassifier(
            max_iter=200,
            learning_rate=0.1,
            max_depth=10,
            early_stopping=True,
            validation_fraction=0.1,
            n_iter_no_change=10,
            random_state=42
        )
    }

    # Train and evaluate models
    results = {}
    for name, model in models.items():
        print(f"\nTraining {name}...")
        
        model.fit(X_train_red, y_train_bal)
        
        if name == "Linear SVM (Fast)":
            y_pred = model.predict(X_test_red)
            y_proba = model.decision_function(X_test_red)
        else:
            y_pred = model.predict(X_test_red)
            y_proba = model.predict_proba(X_test_red)[:, 1] if hasattr(model, "predict_proba") else [0] * len(X_test_red)

        acc = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        roc_auc = roc_auc_score(y_test, y_proba)
        fpr, fnr = calculate_fpr_fnr(y_test, y_pred)

        results[name] = {
            'f1': f1,
            'roc_auc': roc_auc,
            'fpr': fpr,
            'fnr': fnr,
            'model': model
        }

        print(f"{name} Performance:")
        print(f"Accuracy: {acc:.4f}")
        print(f"F1 Score: {f1:.4f}")
        print(f"ROC-AUC: {roc_auc:.4f}")
        print(f"False Positive Rate: {fpr:.4f}")
        print(f"False Negative Rate: {fnr:.4f}")
        print(classification_report(y_test, y_pred))
        print("-" * 40)

    # Threshold tuning for Logistic Regression
    if "Logistic Regression (Balanced)" in results:
        print("\nThreshold Tuning for Logistic Regression...")
        logreg = results["Logistic Regression (Balanced)"]['model']
        calibrated = CalibratedClassifierCV(logreg, cv=3)
        calibrated.fit(X_train_red, y_train_bal)

        y_probs = calibrated.predict_proba(X_test_red)[:, 1]
        threshold = np.percentile(y_probs[y_test == 1], 25)
        y_pred_tuned = (y_probs >= threshold).astype(int)

        f1_tuned = f1_score(y_test, y_pred_tuned)
        roc_auc_tuned = roc_auc_score(y_test, y_probs)
        fpr_tuned, fnr_tuned = calculate_fpr_fnr(y_test, y_pred_tuned)

        results["Logistic Regression (Tuned)"] = {
            'f1': f1_tuned,
            'roc_auc': roc_auc_tuned,
            'fpr': fpr_tuned,
            'fnr': fnr_tuned,
            'model': calibrated
        }

        print("Tuned Logistic Regression Performance:")
        print(f"F1 Score: {f1_tuned:.4f}")
        print(f"ROC-AUC: {roc_auc_tuned:.4f}")
        print(f"False Positive Rate: {fpr_tuned:.4f}")
        print(f"False Negative Rate: {fnr_tuned:.4f}")
        print(classification_report(y_test, y_pred_tuned))

    # Plot feature importance for Random Forest
    if "Random Forest (Optimized)" in results:
        rf_model = results["Random Forest (Optimized)"]['model']
        
        # Get the actual feature names after preprocessing
        feature_mask = joblib.load("models/selector.pkl").get_support()
        feature_names = np.array(training_columns)[feature_mask]
        
        print("\nPlotting Random Forest feature importance...")
        plot_feature_importance(rf_model, feature_names)

    # Select and save best model by F1 score
    best_model_name = max(results, key=lambda k: results[k]['f1'])
    best_model = results[best_model_name]['model']
    joblib.dump(best_model, "models/binary_model.pkl")
    
    print(f"\nBest Model: {best_model_name}")
    print(f"F1: {results[best_model_name]['f1']:.4f}")
    print(f"ROC-AUC: {results[best_model_name]['roc_auc']:.4f}")
    print(f"False Positive Rate: {results[best_model_name]['fpr']:.4f}")
    print(f"False Negative Rate: {results[best_model_name]['fnr']:.4f}")

if __name__ == "_main_":
    train_csv = "data/UNSW_NB15_training-set.csv"
    test_csv = "data/UNSW_NB15_testing-set.csv"
    train_and_evaluate(train_csv, test_csv)
    

