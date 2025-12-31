import os
import subprocess

# --- PROJECT CONFIGURATION ---
MY_NAME = "Ritish Bhatt"
MY_GITHUB = "RitishB05"
COLLABORATOR_NAME = "Bibhuti"
COLLABORATOR_GITHUB = "VESUVIUS9"
REPO_NAME = "Network-Intrusion-Detection-System"

# --- 1. GENERATE REQUIREMENTS.TXT ---
requirements_text = "pandas\nnumpy\nmatplotlib\nseaborn\nscikit-learn\nflask\nxgboost\njoblib"

# --- 2. GENERATE DETAILED README.MD ---
# We use a list and join it to avoid triple-quote SyntaxErrors
readme_lines = [
    "# Network Intrusion Detection System (NIDS) 🛡️\n",
    "**Collaborative Research Project | Machine Learning & Cybersecurity**\n\n",
    "## 👥 Authors & Contributions\n",
    "This project was a joint development effort between:\n",
    f"* **{MY_NAME}** (https://github.com/{MY_GITHUB})\n",
    f"* **{COLLABORATOR_NAME}** (https://github.com/{COLLABORATOR_GITHUB})\n\n",
    "### Author Contribution Breakdown:\n",
    f"* **{MY_NAME}**: Engineered the core Machine Learning pipeline, including Exploratory Data Analysis (EDA), feature scaling, and the implementation of Random Forest and XGBoost classifiers.\n",
    f"* **{COLLABORATOR_NAME}**: Developed the **Flask-based Dashboard**, static asset integration, and real-time visualization of intrusion alerts and model performance metrics.\n\n",
    "---\n\n",
    "## 📌 Project Overview\n",
    "This system utilizes the **UNSW-NB15 dataset** to identify and classify digital network intrusions. It leverages Machine Learning to distinguish between legitimate traffic and malicious activities such as DoS, Fuzzers, and Exploits.\n\n",
    "### 📁 Repository Structure\n",
    "* **/dashboard**: Flask web interface for real-time monitoring and visualization.\n",
    "* **/src**: Core logic for packet classification and traffic analysis.\n",
    "* **/models**: Saved pre-trained models for immediate inference.\n",
    "* **/notebooks**: Detailed logs of training, testing, and hyperparameter tuning.\n",
    "* **/plots**: Performance visualizations including Confusion Matrices and ROC curves.\n\n",
    "## 📊 Evaluation & Results\n",
    "The model's efficacy is demonstrated through rigorous evaluation metrics:\n\n",
    "| Intrusion Confusion Matrix | Network Feature Importance |\n",
    "| :---: | :---: |\n",
    "| ![Matrix](plots/confusion_matrix.png) | ![Features](plots/feature_importance.png) |\n\n",
    "## 🚀 Setup & Execution\n",
    "1. **Environment Setup**:\n",
    "   ```bash\n",
    "   pip install -r requirements.txt\n",
    "   ```\n",
    "2. **Launch Dashboard**:\n",
    "   ```bash\n",
    "   python dashboard/app.py\n",
    "   ```\n",
    "3. **Access**: Open `http://localhost:5000` in your web browser.\n"
]

def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")

def main():
    # 1. Write metadata files
    with open("requirements.txt", "w", encoding="utf-8") as f:
        f.write(requirements_text)
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.writelines(readme_lines)
        
    with open(".gitignore", "w", encoding="utf-8") as f:
        f.write("data/\n__pycache__/\n.vscode/\n*.pyc\n.DS_Store")
    
    print("✅ Requirements, README, and .gitignore generated successfully.")

    # 2. Git Automation
    if not os.path.exists(".git"):
        run_command("git init")
    
    run_command("git add .")
    run_command('git commit -m "Final NIDS push: Integrated Flask Dashboard and ML models"')
    run_command("git branch -M main")
    
    remote_url = f"https://github.com/{MY_GITHUB}/{REPO_NAME}.git"
    try:
        run_command(f"git remote add origin {remote_url}")
    except:
        run_command(f"git remote set-url origin {remote_url}")
    
    print(f"\n🚀 SUCCESS! Now perform these final steps:")
    print(f"1. Create the repo '{REPO_NAME}' on your GitHub account.")
    print(f"2. Run: git push -u origin main")
    print(f"3. Add {COLLABORATOR_GITHUB} as a collaborator in GitHub settings.")

if __name__ == "__main__":
    main()