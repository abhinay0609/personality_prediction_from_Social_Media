# personality_prediction_from_Social_Media
Internpro AI ML Internship 

This repository contains my work  for the InternPro AI/ML Internship (June 2025 - July 2025).

## 📅 Week 1 Summary

- ✅ **Project Understanding** – What the project is about and why it matters
- 📊 **Dataset Selection** – Chose MBTI dataset (Reddit posts + personality types)   [Dataset](https://www.kaggle.com/datasets/datasnaek/mbti-type/data)
- 🧹 **Text Preprocessing** – Lowercasing, punctuation removal, stopwords
- 🔢 **Feature Extraction** – Applied TF-IDF using sklearn
- 📝 **Logged daily progress** and prepared weekly report

## 📅 Week 2 Summary

- ⚙️ Modeling: Tried Logistic Regression, Linear SVM, and RBF SVM
- 📊 Evaluation: Used Accuracy, Precision, Recall, F1-score
- 🧠 Tuning Concepts: Understood C & gamma using visual plots
- 🏆 Best Model: RBF SVM (Balanced results & non-linear fit)

## 📅 Week 3 Summary
- ⚖️ Performed class imbalance analysis using EDA; identified severe underrepresentation in MBTI types like ESFJ, ESTJ.
- 🧹 Applied advanced preprocessing techniques to clean and transform raw social media text more effectively.
- ⚙️ Implemented class_weight='balanced' in Logistic Regression, SVM, and RBF-SVM to improve fairness across rare classes.
- 📊 Achieved a notable macro F1 improvement from 0.46 → 0.52 and confirmed performance boost using multiple evaluation metrics.

## Week 4 Summary
- 🔍 Used RandomizedSearchCV to tune key hyperparameters like C and gamma for both Linear and RBF SVM.
- ⚡ Optimized models efficiently without overloading compute (used limited search space + 3-fold CV).
- ✅ Final comparison showed Logistic Regression as best with Accuracy = 0.65, Macro F1 = 0.52, Weighted F1 = 0.65.
- 📦 Saved trained model and vectorizer using joblib for deployment in the next phase.

## Final Project Highlights / Summary
- 🤖 Built an end-to-end NLP-based machine learning model to predict MBTI personality types from raw social media posts.
- 🧠 Explored multiple models (Logistic Regression, SVM, RBF SVM), applied class balancing, and tuned hyperparameters for fair classification.
- 📈 Achieved 65% accuracy and 0.52 macro F1-score with Logistic Regression — showing significant handling of imbalanced classes.
- 💾 Successfully saved model artifacts (.pkl files) for future deployment (e.g., Streamlit or Flask).



