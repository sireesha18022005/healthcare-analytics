# 🏥 Healthcare Analytics Dashboard

> End-to-end Data Analytics project analyzing 500+ patient records using Python, SQL, Excel, and Power BI.

---

## 📌 Project Overview

This project builds a complete healthcare analytics pipeline that:
- Generates and analyzes 500 patient records
- Performs Exploratory Data Analysis (EDA)
- Stores and queries data using SQL
- Predicts patient readmission using Machine Learning
- Visualizes insights through an interactive Streamlit dashboard

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Data processing, EDA, ML |
| Pandas & NumPy | Data manipulation |
| Matplotlib & Seaborn | Data visualization |
| SQLite | Database & SQL queries |
| Scikit-learn | Machine Learning (Random Forest, Logistic Regression) |
| Streamlit | Interactive dashboard |
| Excel | Pivot Tables, VLOOKUP, XLOOKUP, INDEX MATCH, Dashboard |
| Power BI | Interactive dashboard with slicers and cards |

---

## 📁 Project Structure

```
healthcare-analytics/
├── generate_data.py        # Generate 500 patient records
├── eda.py                  # Exploratory Data Analysis + Charts
├── sql.py                  # SQLite database + SQL queries
├── ml_model.py             # Random Forest & Logistic Regression
├── dashboard.py            # Streamlit interactive dashboard
├── charts/                 # Saved EDA visualizations
│   ├── diagnosis_distribution.png
│   ├── readmission_rate.png
│   ├── age_distribution.png
│   └── avg_stay.png
└── README.md
```

---

## ▶️ How to Run

### 1. Install Dependencies
```bash
pip install pandas numpy matplotlib seaborn scikit-learn streamlit
```

### 2. Generate Dataset
```bash
python generate_data.py
```

### 3. Run EDA
```bash
python eda.py
```

### 4. Run SQL Queries
```bash
python sql.py
```

### 5. Train ML Model
```bash
python ml_model.py
```

### 6. Launch Dashboard
```bash
streamlit run dashboard.py
```

---

## 📊 Key Insights

- **500 patient records** analyzed across 7 diagnoses
- **30% readmission rate** identified
- **Random Forest accuracy: 72%+** for readmission prediction
- **Avg hospital stay: 10.2 days**
- **Total revenue analyzed: ₹2.6 Crore+**

---

## 📈 Dashboard Features

- 🔍 **Filters** — by Diagnosis and Gender
- 📊 **KPI Cards** — Total Patients, Avg Cost, Avg Stay, Readmitted
- 📉 **Charts** — Diagnosis distribution, Readmission rate, Cost by Outcome
- 📋 **Data Table** — Full patient records with filters

---

## 🤖 ML Model Results

| Model | Accuracy |
|-------|---------|
| Logistic Regression | ~65% |
| Random Forest | ~72% |

---

## 👩‍💻 Author

**Sireesha R**
- 📧 sireesharaju525@gmail.com
- 🔗 [LinkedIn](https://www.linkedin.com/in/sireesha-siri-6a70b52bb)
- 💻 [GitHub](https://github.com/sireesha18022005)
- 🏫 B.E. Data Science — SVIT, Bengaluru (VTU)

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).
