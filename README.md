# 🎓 Student Performance Prediction

A Machine Learning project that predicts student academic performance based on demographic, educational, and examination-related factors.

The application provides an interactive web interface built with **Streamlit**, allowing users to train the model and predict student performance using various input features such as gender, parental education, lunch type, test preparation course, and subject scores.

---

## 📌 Project Overview

Student academic performance depends on multiple factors including family background, educational support, and previous academic scores.

This project uses Machine Learning techniques to analyze student data and predict the overall student performance score based on:

- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Math Score
- Reading Score
- Writing Score

The model is deployed through a user-friendly Streamlit web application.

---

## 🚀 Features

### Model Training
- Data Ingestion
- Data Transformation
- Feature Engineering
- Model Training
- Model Evaluation
- Best Model Selection

### Prediction Interface
- Interactive Streamlit UI
- Real-time predictions
- Easy-to-use form inputs
- Instant performance score prediction

---

## 🏗️ Project Structure

```text
Student-Performance-Prediction/
│
├── notebook/
│   └── EDA.ipynb
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │
│   ├── pipelines/
│   │   ├── trainer_pipeline.py
│   │   ├── predict_pipeline.py
│   │
│   ├── logger.py
│   ├── custom_exception.py
│   └── utils.py
│
├── artifacts/
│   ├── model.pkl
│   ├── preprocessor.pkl
│
├── app.py
├── requirements.txt
├── setup.py
└── README.md
```

---

## 📊 Dataset Features

| Feature | Description |
|----------|------------|
| Gender | Male/Female |
| Race/Ethnicity | Student Group Category |
| Parental Level of Education | Education qualification of parents |
| Lunch Type | Standard / Free-Reduced |
| Test Preparation Course | Completed / None |
| Math Score | Student Math Marks |
| Reading Score | Student Reading Marks |
| Writing Score | Student Writing Marks |

### Target Variable

**Predicted Total Performance Score**

---

## ⚙️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- CatBoost
- XGBoost
- Random Forest
- Streamlit
- Pickle
- Git & GitHub

---

## 🧠 Machine Learning Pipeline

### 1. Data Ingestion
- Load dataset
- Split into train and test sets

### 2. Data Transformation
- Handle categorical variables
- Apply preprocessing pipeline
- Feature encoding

### 3. Model Training
Multiple regression models are trained and evaluated:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor
- CatBoost Regressor
- AdaBoost Regressor

### 4. Model Evaluation
- R² Score
- Best model selection
- Model serialization

---

## 🖥️ Streamlit Application

### Home Page

The application contains two modules:

### Train Model
Runs:

- Data Ingestion
- Data Transformation
- Model Training

with a single button click.

### Make Prediction

Users can enter:

- Gender
- Race/Ethnicity
- Parental Education
- Lunch Type
- Test Preparation Course
- Math Score
- Reading Score
- Writing Score

and receive the predicted student performance score instantly.

---

## 📷 Application Screenshots

### Prediction Interface

The application provides an intuitive interface where users can enter student information and predict performance scores in real time.

---

## 🔧 Installation

### Clone Repository

```bash
git clone https://github.com/samkhan0007/ML_Project.git
```

### Move into Project Directory

```bash
cd ML_Project
```

### Create Virtual Environment

```bash
python -m venv myenv
```

### Activate Environment

#### Windows

```bash
myenv\Scripts\activate
```

#### Linux/Mac

```bash
source myenv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Application will start on:

```text
http://localhost:8501
```

---

## 📈 Example Prediction

### Input

```text
Gender: Male
Race/Ethnicity: Group A
Parental Education: High School
Lunch Type: Standard
Test Preparation Course: None
Math Score: 50
Reading Score: 50
Writing Score: 50
```

### Output

```text
Predicted Total Performance Score: XX.XX
```

---

## 🎯 Future Improvements

- Cloud Deployment (AWS/Azure/GCP)
- Docker Containerization
- Model Monitoring
- Performance Analytics Dashboard
- User Authentication
- Batch Predictions via CSV Upload

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Create a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Your Name**

Machine Learning Engineer

If you found this project useful, consider giving it a ⭐ on GitHub.
