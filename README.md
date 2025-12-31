# Network Intrusion Detection System (NIDS) 🛡️
**Collaborative Research Project | Machine Learning & Cybersecurity**

## 👥 Authors & Contributions
This project was a joint development effort between:
* **Ritish Bhatt** (https://github.com/RitishB05)
* **Bibhuti** (https://github.com/VESUVIUS9)

### Author Contribution Breakdown:
* **Ritish Bhatt**: Engineered the core Machine Learning pipeline, including Exploratory Data Analysis (EDA), feature scaling, and the implementation of Random Forest and XGBoost classifiers.
* **Bibhuti**: Developed the **Flask-based Dashboard**, static asset integration, and real-time visualization of intrusion alerts and model performance metrics.

---

## 📌 Project Overview
This system utilizes the **UNSW-NB15 dataset** to identify and classify digital network intrusions. It leverages Machine Learning to distinguish between legitimate traffic and malicious activities such as DoS, Fuzzers, and Exploits.

### 📁 Repository Structure
* **/dashboard**: Flask web interface for real-time monitoring and visualization.
* **/src**: Core logic for packet classification and traffic analysis.
* **/models**: Saved pre-trained models for immediate inference.
* **/notebooks**: Detailed logs of training, testing, and hyperparameter tuning.
* **/plots**: Performance visualizations including Confusion Matrices and ROC curves.

## 📊 Evaluation & Results
The model's efficacy is demonstrated through rigorous evaluation metrics:

| Intrusion Confusion Matrix | Network Feature Importance |
| :---: | :---: |
| ![Matrix](plots/confusion_matrix.png) | ![Features](plots/feature_importance.png) |

## 🚀 Setup & Execution
1. **Environment Setup**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Launch Dashboard**:
   ```bash
   python dashboard/app.py
   ```
3. **Access**: Open `http://localhost:5000` in your web browser.
