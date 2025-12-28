# Employee Salary Prediction using Machine Learning

This project predicts an employee’s salary based on factors such as **age**, **experience**, **department**, and **education** using **Machine Learning** techniques.

It demonstrates a complete ML workflow including data preprocessing, feature engineering, model training, evaluation, and prediction.

---

## 🚀 Project Overview

- **Domain:** Machine Learning
- **Algorithm Used:** Linear Regression
- **Use Case:** HR Analytics / Salary Estimation
- **Language:** Python

The model helps organizations estimate a fair salary based on employee attributes.

---

## 📊 Dataset Details

**Columns used:**
- `name`
- `age`
- `department`
- `education`
- `experience`
- `salary`

The dataset contains missing values and categorical features to simulate real-world data.

---

## 🔧 Data Preprocessing

Steps performed:
1. Handled missing values using median
2. Dropped non-informative column (`name`)
3. Applied **One-Hot Encoding** to:
   - `department`
   - `education`
4. Applied **Standard Scaling** to numerical features:
   - `age`
   - `experience`
5. Split data into training and testing sets

---

## 🤖 Model Training

- Algorithm: **Linear Regression**
- Evaluation Metrics:
  - R² Score
  - Mean Absolute Error (MAE)

The model achieves a good R² score, indicating effective learning from the data.

---

## 📈 Model Evaluation

- **R² Score:** ~0.65 – 0.75 (varies with data split)
- **MAE:** Shows reasonable prediction error for salary estimation

---

## 🧪 Salary Prediction (User Input)

The model allows users to input:
- Age
- Experience

And predicts the **expected salary** based on trained data.

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn

---

## 📂 Project Structure

