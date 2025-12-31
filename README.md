# Network-Intrusion-Detection-System 🛡️
![Python](https://img.shields.io/badge/python-3.8+-blue.svg) ![Flask](https://img.shields.io/badge/flask-v2.0-lightgrey.svg) ![ML](https://img.shields.io/badge/Random%20Forest-ROC--AUC%200.98-green.svg)

## 📌 Project Overview
Developed at **UIET, Panjab University**, this project presents a robust binary classification system for detecting network intrusions. Using the **UNSW-NB15 dataset**, the system identifies malicious activity by analyzing 5 critical features: `duration`, `protocol`, `service`, `source bytes`, and `destination bytes`.

## 👥 Authors & Academic Collaboration
| Author | Affiliation | Role |
| :--- | :--- | :--- |
| **[Ritish Bhatt](https://github.com/RitishB05)** | UIET, Panjab University | ML Pipeline, Preprocessing, Model Training. |
| **[Bibhuti Singha](https://github.com/VESUVIUS9)** | UIET, Panjab University | Flask Dashboard, UI Design, Real-time Predictions. |

## 🔬 Research Highlights (from PDF)
* **Feature Selection**: Focused on a high-impact subset of 5 features to minimize computational overhead and data leakage.
* **Comparative Analysis**: Evaluated Logistic Regression, Random Forest, Linear SVM, and HistGradientBoosting.
* **Champion Model**: **Random Forest** achieved the highest performance with an **F1-score of 0.92** and an **ROC-AUC of 0.98**.
* **Real-time Deployment**: Integrated a Flask-based web dashboard for practical deployment in SOC environments.

## 📊 Evaluation & Visuals
Below are the forensic results extracted from the `plots/` directory:

### 1. Model Performance (Confusion Matrix)
![Confusion Matrix](plots/confusion_matrix.png)
*This plot demonstrates the model's high sensitivity in distinguishing between normal and malicious traffic.*

### 2. Training Dynamics
![Training Curve](plots/training_curve.png)

### 3. Receiver Operating Characteristic (ROC)
![ROC Curve](plots/roc_curve.png)
*Our Random Forest model achieved a 0.98 AUC, indicating near-perfect classification capabilities.*

## 📂 Repository Architecture
```text
├── dashboard/      # Flask Web Application (app.py, templates, static)
├── models/         # Serialized ML Models (.pkl files)
├── notebooks/      # Data Preprocessing and Training Notebooks
├── src/            # Core Python modules for inference logic
├── plots/          # Evaluation graphs (Confusion Matrix, ROC, etc.)
└── Network_Intrusion_Detection_Report.pdf # Full Research Paper
```

## 🚀 Installation & Usage
1. **Clone & Install**:
   ```bash
   git clone [https://github.com/](https://github.com/)RitishB05/Network-Intrusion-Detection-System.git
   pip install -r requirements.txt
   ```
2. **Run Application**:
   ```bash
   python dashboard/app.py
   ```
