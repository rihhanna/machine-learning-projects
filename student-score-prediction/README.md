# 🎓 Student Score Prediction | End-to-End Machine Learning Project

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Machine Learning](https://img.shields.io/badge/ML-Regression-green)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Linear%20Regression-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Dataset](https://img.shields.io/badge/Dataset-Real%20World-blueviolet)

---

## 👩‍💻 Author

**Rehana Hassan**  
Software Engineering Student | Machine Learning Portfolio Builder 🚀  

---

## 📊 GitHub Stats

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=rihhanna&show_icons=true&theme=tokyonight)

---

## 📌 Project Overview

This project predicts a student's **Math Score** using machine learning based on academic and demographic features.

It is part of my **Machine Learning Journey**, focused on building real-world projects step-by-step.

---

## 🎯 Objective

Build a regression model that predicts student performance using:

- Demographic data
- Study habits
- Exam preparation
- Reading & Writing scores

---

## 🧠 Problem Type

### Regression vs Classification

| Type | Output | Example |
|------|--------|--------|
| Regression | Numerical value | Math Score = 85 |
| Classification | Category | Pass / Fail |

👉 This project is a **Regression problem**.

---

## 🏗️ Model Pipeline


Data Collection
↓
Data Preprocessing (Encoding, Cleaning)
↓
Train/Test Split
↓
Linear Regression Model
↓
Prediction (Math Score)


---

## 📊 Dataset

- Source: Kaggle / UCI Repository  
- Samples: 1000+ students  
- Target: `math score`

### Features:
- Gender  
- Race/Ethnicity  
- Parental Education  
- Lunch Type  
- Test Preparation Course  
- Reading Score  
- Writing Score  

---

## 📈 Model Performance

- R² Score: **0.88**
- Explained Variance: **88%**

---

## 📊 Visualizations

- Score Distribution → `images/math_score_distribution.png`  
- Reading vs Math → `images/reading_vs_math.png`  
- Writing vs Math → `images/writing_vs_math.png`  
- Actual vs Predicted → `images/actual_vs_predicted.png`  

---

## 🚀 Run the Project

### Install dependencies

pip install -r requirements.txt
Run Streamlit app
streamlit run app.py
🧪 Sample Prediction
input_data = [[
    "female",
    "group B",
    "bachelor's degree",
    "standard",
    "completed",
    72,
    74
]]

# Predicted Output
Math Score → 78.5

##🔍 Key Insights
Reading score strongly affects math performance
Writing score is highly correlated with math score
Test preparation improves results
Linear Regression is a strong baseline model


##🛠️ Tech Stack
Python 🐍
Pandas
NumPy
Matplotlib
Scikit-learn


##📁 Project Structure
student-score-prediction/
│
├── data/
├── images/
├── notebook/
├── app.py
├── model.pkl
├── README.md


##🚀 Future Improvements
Try Random Forest / XGBoost
Hyperparameter tuning
Deploy on Streamlit Cloud
Feature importance analysis
Build dashboard UI

##⭐ Support

If you like this project:

⭐ Star the repository
📌 Follow my ML journey
🚀 More projects coming soon

🔥 Next Project

Pass/Fail Classification Model
