import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("charts", exist_ok=True)

df = pd.read_csv("data/patient_data.csv")

print("===== BASIC INFO =====")
print("Shape:", df.shape)
print("\nMissing Values:")
print(df.isnull().sum())
print("\nBasic Stats:")
print(df.describe())

# Chart 1 - Diagnosis Distribution
plt.figure(figsize=(10, 5))
df["Diagnosis"].value_counts().plot(kind="bar", color="steelblue")
plt.title("Patient Count by Diagnosis")
plt.xlabel("Diagnosis")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("charts/diagnosis_distribution.png")
plt.close()
print("✅ Chart 1 saved!")

# Chart 2 - Readmission Rate
plt.figure(figsize=(6, 5))
df["Readmitted"].value_counts().plot(kind="pie", autopct="%1.1f%%", colors=["#ff6b6b","#6bcb77"])
plt.title("Readmission Rate")
plt.tight_layout()
plt.savefig("charts/readmission_rate.png")
plt.close()
print("✅ Chart 2 saved!")

# Chart 3 - Age Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["Age"], bins=20, kde=True, color="purple")
plt.title("Age Distribution")
plt.tight_layout()
plt.savefig("charts/age_distribution.png")
plt.close()
print("✅ Chart 3 saved!")

# Chart 4 - Avg Stay by Diagnosis
plt.figure(figsize=(10, 5))
df.groupby("Diagnosis")["HospitalStayDays"].mean().sort_values().plot(kind="barh", color="coral")
plt.title("Avg Hospital Stay by Diagnosis")
plt.tight_layout()
plt.savefig("charts/avg_stay.png")
plt.close()
print("✅ Chart 4 saved!")

print("\n✅ EDA Complete! Charts saved in charts/ folder")