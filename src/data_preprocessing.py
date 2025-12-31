import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder, StandardScaler

def load_data(train_path, test_path):
    """Load training and testing data from CSV files."""
    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)
    return train_df, test_df

def preprocess_data(df, ref_columns=None, scaler=None, label_encoders=None):
    """Preprocess data by encoding categorical columns and scaling numerical columns."""
    # Drop 'attack_cat' if present
    if 'attack_cat' in df.columns:
        df = df.drop('attack_cat', axis=1)

    # Separate features and target
    if 'label' in df.columns:
        y = df['label']
        X = df.drop('label', axis=1)
    else:
        y = None
        X = df.copy()

    # Align columns with ref_columns if provided
    if ref_columns is not None:
        X = X.reindex(columns=ref_columns, fill_value=0)

    # Identify categorical and numerical columns
    categorical_cols = ['proto', 'service']  # Explicitly define categorical columns
    numerical_cols = ['dur', 'sbytes', 'dbytes']  # Explicitly define numerical columns

    # Initialize or use provided label encoders
    if label_encoders is None:
        label_encoders = {}
        for col in categorical_cols:
            if col in X.columns:
                le = LabelEncoder()
                X[col] = le.fit_transform(X[col].astype(str))
                label_encoders[col] = le
    else:
        for col in categorical_cols:
            if col in X.columns and col in label_encoders:
                le = label_encoders[col]
                # Handle unseen categories by mapping to a default (first class)
                X[col] = X[col].apply(lambda x: x if x in le.classes_ else le.classes_[0])
                X[col] = le.transform(X[col])
            elif col in X.columns:
                X[col] = 0  # Default for missing encoders

    # Initialize or use provided scaler
    if scaler is None:
        scaler = StandardScaler()
        X[numerical_cols] = scaler.fit_transform(X[numerical_cols])
    else:
        X[numerical_cols] = scaler.transform(X[numerical_cols])

    # Ensure all columns are numerical
    X_scaled = X.values
    return X_scaled, y, X.columns.tolist(), scaler, label_encoders

if __name__ == "__main__":
    # Paths to data
    train_path = "data/UNSW_NB15_training-set.csv"
    test_path = "data/UNSW_NB15_testing-set.csv"
    
    # Load data
    train_df, test_df = load_data(train_path, test_path)
    
    # Preprocess training data
    training_columns = ['dur', 'proto', 'service', 'sbytes', 'dbytes']
    X_train, y_train, train_columns, fitted_scaler, label_encoders = preprocess_data(
        train_df[training_columns + ['label']]
    )
    print("Training data shape:", X_train.shape)
    
    # Save preprocessing artifacts
    joblib.dump(training_columns, "models/training_columns.pkl")
    joblib.dump(fitted_scaler, "models/scaler.pkl")
    joblib.dump(label_encoders, "models/label_encoders.pkl")
    print("Saved training_columns:", training_columns)
    
    # Preprocess test data
    X_test, y_test, _, _, _ = preprocess_data(
        test_df[training_columns + ['label']],
        ref_columns=training_columns,
        scaler=fitted_scaler,
        label_encoders=label_encoders
    )
    print("Test data shape:", X_test.shape)