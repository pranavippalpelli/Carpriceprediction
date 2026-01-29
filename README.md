# 🚗 Car Price Prediction Web Application

This project is a **Django-based web application** that predicts the price of a car using a **Machine Learning regression model**.  
The model is trained using real-world car data and integrated into a Django backend to provide price predictions based on user input.

---

## 📌 Project Overview

The application allows users to enter car details such as:
- Year of manufacture
- Mileage
- Tax
- MPG
- Engine size
- Fuel type
- Transmission type
- Car model

Based on these inputs, the system predicts the **estimated car price** using a trained Machine Learning model.

---

## 🧠 Machine Learning Details

- **Algorithm Used**: Linear Regression  
- **Library**: scikit-learn  
- **Preprocessing**:
  - One-Hot Encoding for categorical features
  - Standard Scaling for numerical features
- **Model Integration**:
  - Trained model and scaler are saved and loaded in Django
  - Input data is preprocessed exactly the same way as during training

This ensures consistency between training and prediction.

---

## 🛠 Tech Stack

- **Backend**: Django (Python)
- **Machine Learning**: scikit-learn, Pandas, NumPy
- **Frontend**: HTML (Django Templates)
- **Version Control**: Git & GitHub

---

## ✨ Features

- User-friendly web form for input
- Machine Learning–based price prediction
- Proper preprocessing and feature alignment
- Error-free ML–Django integration
- Clean and modular project structure
