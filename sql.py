import sqlite3
import pandas as pd

df = pd.read_csv("data/patient_data.csv")

conn = sqlite3.connect("data/hospital.db")
df.to_sql("patients", conn, if_exists="replace", index=False)
print("✅ Data saved to database!")

cursor = conn.cursor()

print("\n1. Total Patients:")
cursor.execute("SELECT COUNT(*) FROM patients")
print(cursor.fetchone()[0])

print("\n2. Readmission Count:")
cursor.execute("SELECT Readmitted, COUNT(*) FROM patients GROUP BY Readmitted")
for row in cursor.fetchall():
    print(row)

print("\n3. Avg Stay by Diagnosis:")
cursor.execute("""
    SELECT Diagnosis, ROUND(AVG(HospitalStayDays), 2) as AvgStay
    FROM patients
    GROUP BY Diagnosis
    ORDER BY AvgStay DESC
""")
for row in cursor.fetchall():
    print(row)

print("\n4. Top Diagnosis by Readmission:")
cursor.execute("""
    SELECT Diagnosis, COUNT(*) as Count
    FROM patients
    WHERE Readmitted = 'Yes'
    GROUP BY Diagnosis
    ORDER BY Count DESC
""")
for row in cursor.fetchall():
    print(row)

conn.close()
print("\n✅ SQL Complete!")
