
# 🎓 Student Score Prediction | End-to-End Machine Learning Project

![Python](https://img.shields.io/badge/Python-3.10-blue)
![ML](https://img.shields.io/badge/Machine%20Learning-Regression-green)
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

It is part of my **Machine Learning Journey**, where I build real-world projects step-by-step to strengthen my data science skills.

---

## 🎯 Objective

To build a regression model that predicts student performance using:

- Demographic data
- Study habits
- Exam preparation
- Other subject scores

---

## 🧠 Machine Learning Type

### 📌 Regression vs Classification

| Type | Description | Example |
|------|------------|---------|
| Regression | Predicts a number | Math Score = 85 |
| Classification | Predicts a category | Pass / Fail |

👉 This project uses **Regression** because we predict a numeric score.

---

## 🏗️ Model Architecture

```
```
Input Features
↓
Data Preprocessing (Encoding)
↓
Train/Test Split
↓
Linear Regression Model
↓
Prediction (Math Score)

```
````

---

## 📊 Dataset Information

- Source: Kaggle / UCI Repository  
- Records: 1000+ students  
- Target: `math score`

### Features:

- Gender
- Race/Ethnicity
- Parental Education
- Lunch
- Test Preparation Course
- Reading Score
- Writing Score

---

## 📈 Model Performance

- **R² Score:** 0.88  
- **Accuracy (Explained Variance):** 88%

---

## 📊 Visualizations

### 📉 Score Distribution
![Distribution](../images/math_score_distribution.png)

### 📊 Reading vs Math
![Reading](../images/reading_vs_math.png)

### 📊 Writing vs Math
![Writing](../images/writing_vs_math.png)

### 📊 Actual vs Predicted
![Prediction](../images/actual_vs_predicted.png)

---

## 🚀 Live Demo (Optional)

You can run this project using Streamlit:

```bash
streamlit run app.py
````
```
👉 App features:

* Input student details
* Predict math score instantly
* Simple UI for real-time prediction
```
---

## 🧪 Try It Yourself

```python id="try1"
# Example input
input_data = [[
    "female",
    "group B",
    "bachelor's degree",
    "standard",
    "completed",
    72,
    74
]]

# Output
Predicted Math Score → 78.5
```

---
```

## 🔍 Key Insights

* Reading score strongly influences math score
* Writing score is highly correlated
* Test preparation improves performance
* Linear Regression is a strong baseline model

---

## 🛠️ Tech Stack

* Python 🐍
* Pandas
* NumPy
* Matplotlib
* Scikit-learn

---

## 📁 Project Structure

```
```
student-score-prediction/
│
├── data/
├── images/
├── notebook/
├── model.pkl
├── app.py
├── README.md
```
```
---

## 📌 Future Improvements

* Try Random Forest / XGBoost
* Hyperparameter tuning
* Deploy on Streamlit Cloud
* Add feature importance visualization
* Build web UI dashboard

---

## ⭐ Support

If you like this project:

⭐ Star this repo
📌 Follow my ML journey
🚀 More projects coming soon

---

## 🔥 Next Project

👉 Pass/Fail Classifier (Classification Project)

```

---


