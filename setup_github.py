import os
import subprocess

# --- PROJECT CONFIGURATION ---
MY_NAME = "Ritish Bhatt"
MY_GITHUB = "RitishB05"
COLLABORATOR_NAME = "Bibhuti Singha"
COLLABORATOR_GITHUB = "VESUVIUS9"
REPO_NAME = "Network-Intrusion-Detection-System"

# --- 1. REQUIREMENTS ---
requirements = "pandas\nnumpy\nmatplotlib\nseaborn\nscikit-learn\nflask\nxgboost\njoblib"

# --- 2. DETAILED README SECTIONS ---
readme_lines = [
    f"# {REPO_NAME} 🛡️\n",
    "![Python](https://img.shields.io/badge/python-3.8+-blue.svg) ",
    "![Flask](https://img.shields.io/badge/flask-v2.0-lightgrey.svg) ",
    "![ML](https://img.shields.io/badge/Random%20Forest-ROC--AUC%200.98-green.svg)\n\n",
    
    "## 📌 Project Overview\n",
    "Developed at **UIET, Panjab University**, this project presents a robust binary classification system for detecting network intrusions. Using the **UNSW-NB15 dataset**, the system identifies malicious activity by analyzing 5 critical features: `duration`, `protocol`, `service`, `source bytes`, and `destination bytes`.\n\n",

    "## 👥 Authors & Academic Collaboration\n",
    "| Author | Affiliation | Role |\n",
    "| :--- | :--- | :--- |\n",
    f"| **[{MY_NAME}](https://github.com/{MY_GITHUB})** | UIET, Panjab University | ML Pipeline, Preprocessing, Model Training. |\n",
    f"| **[{COLLABORATOR_NAME}](https://github.com/{COLLABORATOR_GITHUB})** | UIET, Panjab University | Flask Dashboard, UI Design, Real-time Predictions. |\n\n",

    "## 🔬 Research Highlights (from PDF)\n",
    "* **Feature Selection**: Focused on a high-impact subset of 5 features to minimize computational overhead and data leakage.\n",
    "* **Comparative Analysis**: Evaluated Logistic Regression, Random Forest, Linear SVM, and HistGradientBoosting.\n",
    "* **Champion Model**: **Random Forest** achieved the highest performance with an **F1-score of 0.92** and an **ROC-AUC of 0.98**.\n",
    "* **Real-time Deployment**: Integrated a Flask-based web dashboard for practical deployment in SOC environments.\n\n",

    "## 📊 Evaluation & Visuals\n",
    "Below are the forensic results extracted from the `plots/` directory:\n\n",
    
    "### 1. Model Performance (Confusion Matrix)\n",
    "![Confusion Matrix](plots/confusion_matrix.png)\n",
    "*This plot demonstrates the model's high sensitivity in distinguishing between normal and malicious traffic.*\n\n",
    
    "### 2. Training Dynamics\n",
    "![Training Curve](plots/training_curve.png)\n\n",
    
    "### 3. Receiver Operating Characteristic (ROC)\n",
    "![ROC Curve](plots/roc_curve.png)\n",
    "*Our Random Forest model achieved a 0.98 AUC, indicating near-perfect classification capabilities.*\n\n",

    "## 📂 Repository Architecture\n",
    "```text\n",
    "├── dashboard/      # Flask Web Application (app.py, templates, static)\n",
    "├── models/         # Serialized ML Models (.pkl files)\n",
    "├── notebooks/      # Data Preprocessing and Training Notebooks\n",
    "├── src/            # Core Python modules for inference logic\n",
    "├── plots/          # Evaluation graphs (Confusion Matrix, ROC, etc.)\n",
    "└── Network_Intrusion_Detection_Report.pdf # Full Research Paper\n",
    "```\n\n",

    "## 🚀 Installation & Usage\n",
    "1. **Clone & Install**:\n",
    "   ```bash\n",
    f"   git clone [https://github.com/](https://github.com/){MY_GITHUB}/{REPO_NAME}.git\n",
    "   pip install -r requirements.txt\n",
    "   ```\n",
    "2. **Run Application**:\n",
    "   ```bash\n",
    "   python dashboard/app.py\n",
    "   ```\n"
]

def main():
    # 1. Write the files
    with open("requirements.txt", "w") as f: f.write(requirements)
    with open("README.md", "w", encoding="utf-8") as f: f.writelines(readme_lines)
    with open(".gitignore", "w") as f: f.write("data/\n__pycache__/\n.vscode/\n*.pyc\n.DS_Store")
    
    print("✅ Requirements, Detailed README (from PDF), and .gitignore generated.")

    # 2. Git Logic
    if not os.path.exists(".git"):
        subprocess.run("git init", shell=True)
    
    subprocess.run("git add .", shell=True)
    subprocess.run('git commit -m "Docs: Update detailed README with research paper insights"', shell=True)
    subprocess.run("git branch -M main", shell=True)
    
    remote_url = f"https://github.com/{MY_GITHUB}/{REPO_NAME}.git"
    subprocess.run(f"git remote set-url origin {remote_url}", shell=True)
    
    print(f"\n🚀 Everything is ready! Run: git push -u origin main")

if __name__ == "__main__":
    main()