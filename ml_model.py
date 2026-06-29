import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("charts", exist_ok=True)

df = pd.read_csv("data/patient_data.csv")

# Encode categorical columns
le = LabelEncoder()
df["Gender_enc"] = le.fit_transform(df["Gender"])
df["Diagnosis_enc"] = le.fit_transform(df["Diagnosis"])
df["Outcome_enc"] = le.fit_transform(df["Outcome"])
df["Readmitted_enc"] = le.fit_transform(df["Readmitted"])

features = ["Age", "Gender_enc", "Diagnosis_enc", "HospitalStayDays", "TreatmentCost", "Outcome_enc"]
X = df[features]
y = df["Readmitted_enc"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Logistic Regression
lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)
print(f"Logistic Regression Accuracy: {accuracy_score(y_test, lr_pred)*100:.2f}%")

# Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)
print(f"Random Forest Accuracy: {accuracy_score(y_test, rf_pred)*100:.2f}%")

print("\n===== Classification Report =====")
print(classification_report(y_test, rf_pred, target_names=["Not Readmitted", "Readmitted"]))

# Feature Importance Chart
plt.figure(figsize=(8, 5))
feat_imp = pd.Series(rf.feature_importances_, index=features).sort_values()
feat_imp.plot(kind="barh", color="teal")
plt.title("Feature Importance - Random Forest")
plt.tight_layout()
plt.savefig("charts/feature_importance.png")
plt.close()
print("✅ Feature importance chart saved!")

print("\n✅ ML Model Complete!")