# 🧪 Data-Driven Pitting Corrosion Prediction

A **professional-grade Streamlit web application** for predicting the **pitting potential (Epit, mV SCE)** of stainless steels and Fe-based alloys using **alloy composition** and **environmental conditions**.

---

## 🚀 Overview

This project delivers a robust, **data-driven solution** for estimating corrosion resistance in real-world environments.  
It leverages a **peer-reviewed scientific dataset** and advanced **LightGBM regression modeling** to help **engineers and researchers** assess material performance in various service conditions.

---

## 📥 Inputs

- 🧪 **Alloy Composition (wt.%)**  
  `Al`, `Cr`, `Fe`, `Ni`, `Mo`, `N`, `Mn`, `C`, `Si`

- 💧 **Environmental Conditions**  
  `pH`, `Test Temperature (°C)`, `Chloride Concentration (M)`

---

## 📤 Outputs

- 🔋 **Predicted Pitting Potential (mV SCE)**
- ⚠️ **Corrosion Risk Category**  
  *(Very High, High, Moderate, Low, Very Low)*

---

## ✨ Features

- 📊 **Real-World Data**  
  Trained on a **peer-reviewed corrosion dataset**:  
  `CRA_database_Scientific_Data_Publication_12102020.xlsx`

- 🧬 **Metallurgy-Centric Design**  
  Focused on relevant **alloying elements** and **testing parameters** for Fe-based alloys and stainless steels.

- 🚀 **Advanced Modeling**  
  Built on **LightGBM regression** with robust **feature selection** and **hyperparameter tuning**.

- 🧠 **Interpretability**  
  Risk categories provide **actionable insights** for materials selection.

- 🖥️ **Deployment-Ready**  
  Built using **Streamlit** with a clean, professional interface for real-world application.

---

## 🧾 Example

### ✅ Input:

Fe: 60.0, Cr: 18.0, Ni: 10.0, Mo: 2.0, Al: 0.0, N: 0.0, Mn: 1.0, C: 0.03, Si: 1.0
pH: 7.0
Test Temperature: 25.0°C
Chloride: 0.5 M

### 📈 Output:

Predicted Pitting Potential: 540 mV SCE
Corrosion Risk: Moderate Risk

---

## 🧠 Model

- 📁 **Dataset**:  
  [`CRA_database_Scientific_Data_Publication_12102020.xlsx`](https://figshare.com/articles/dataset/Electrochemical_Metrics_for_Corrosion_Resistant_Alloys/13038257?file=25872246)  
  _Sheet: "Pitting Potential"_

- 🔍 **Features Used**:  
  `Al`, `Cr`, `Fe`, `Ni`, `Mo`, `N`, `Mn`, `C`, `Si`, `pH`, `Test Temperature (°C)`, `Chloride Concentration (M)`

- 🤖 **Model**:  
  **LightGBM Regressor**  
  - Tuned via Optuna
  - Trained on cleaned and engineered features

---

## 🌐 Live Demo

👉 [Click here to try the app](https://corrosion-prediction.onrender.com)

---

## ⚙️ Technologies Used

- **Python 3.13**
- **Streamlit** – Web application framework
- **Pandas / NumPy** – Data processing
- **scikit-learn** – Preprocessing and utilities
- **LightGBM** – Machine learning model
- **Render** – Cloud hosting platform
