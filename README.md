# MINI-PROJECT: Dry Bean Classification using Machine Learning
---
---

## Project Overview
This project focuses on classifying different varieties of dry beans using machine learning techniques. Morphological features of dry beans are used to train and evaluate multiple classification models, and the best-performing model is deployed as a web application.

---

## Dataset
- Dataset Name: Dry Bean Dataset
- Source: UCI Machine Learning Repository
- Number of Instances: ~13,000
- Number of Features: 16 numerical features
- Target Variable: Bean class (multi-class)
- Dataset: Dry Bean Dataset

---

## Methodology
1. Data loading and understanding
2. Exploratory Data Analysis (EDA)
3. Data Preprocessing
4. Feature scaling and data splitting
5. Baseline model implementation 
6. Model evaluation and comparison
7. Hyperparameter tuning
8. Final model selection
9. Feature Importance Analysis
10. Model deployment using Streamlit

---

## Exploratory Data Analysis (EDA) & Pre-processing
- Data shape and basic inspection
- Missing value handling
- Statistical summary
- Feature distribution analysis
- Correlation analysis

---

## Models Used
- Logistic Regression
- K-Nearest Neighbors (KNN)
- Naive Bayes
- Decision Tree
- Random Forest
- Support Vector Machine (SVM)
- CatBoost

---

## Model Evaluation
The models were evaluated using:
- Accuracy
- Precision (Weighted)
- Recall (Weighted)
- F1-score (Weighted)
Results were compared in a single consolidated table

----

## Best Model Selection
- Models were evaluated using **Accuracy** and **Weighted F1-Score**
- **Support Vector Machine (SVM)** achieved the best overall performance
- Hyperparameter tuning further improved model generalization

---

## Deployment
- The final SVM model was saved using Pickle (`model.pkl`)
- A Streamlit web application (`app.py`) was created
- Deployment was done using **Streamlit Community Cloud**
- Users can input feature values and obtain real-time predictions via a browser

---

## Project Structure
- app.py # Streamlit application
- model.pkl # Trained ML model
- requirements.txt # Required libraries
- README.md # Project documentation
- Dry_Bean_Project.ipynb # Jupyter notebook
- Dry_Bean_dataset.csv #raw dataset

---

## Results
- SVM achieved the highest test performance among all models (~92%)
- The model effectively classifies dry bean varieties with high accuracy and F1-score
- Reduced overfitting through hyperparameter tuning
- Balanced performance across multiple classes

---

## Conclusion
This project demonstrates the effectiveness of machine learning in agricultural classification problems and provides a practical deployment-ready solution using Streamlit.

---

## Author
- Name: Fathima Salga
- Project Type: Machine Learning Mini Project
