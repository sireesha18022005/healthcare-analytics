import pandas as pd
import numpy as np
import os

np.random.seed(42)
n = 500

df = pd.DataFrame({
    "PatientID": range(1, n+1),
    "Age": np.random.randint(20, 90, n),
    "Gender": np.random.choice(["Male", "Female"], n),
    "Diagnosis": np.random.choice(["Diabetes", "Heart Disease", "Hypertension", "Pneumonia", "Asthma", "Cancer", "Stroke"], n),
    "HospitalStayDays": np.random.randint(1, 20, n),
    "Readmitted": np.random.choice(["Yes", "No"], n, p=[0.3, 0.7]),
    "Outcome": np.random.choice(["Recovered", "Referred", "Deceased"], n, p=[0.7, 0.2, 0.1]),
    "TreatmentCost": np.round(np.random.uniform(5000, 100000, n), 2)
})

os.makedirs("data", exist_ok=True)
df.to_csv("data/patient_data.csv", index=False)
print("Dataset created!")
print(df.head())