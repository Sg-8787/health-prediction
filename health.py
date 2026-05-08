#libraries for data manipulation and visualization
import pandas as pd
import matplotlib.pyplot as plt

#sample dataset
data = {
    "Age": [22, 45, 35, 50, 29, 60, 40, 55, 33, 48],
    "BMI": [22, 30, 28, 35, 24, 32, 29, 36, 25, 31],
    "Sugar": [90, 160, 140, 180, 95, 200, 150, 190, 110, 170],
    "BP": [110, 150, 140, 160, 115, 170, 145, 165, 120, 155]
}
df = pd.DataFrame(data)

print("📊 Dataset:\n")
print(df)

#statistical summary
print("\n Statistical Summary:\n")
print(df.describe())

#matplotlib visualizations
# Age vs Sugar
plt.figure()
plt.scatter(df["Age"], df["Sugar"])
plt.title("Age vs Sugar Level")
plt.xlabel("Age")
plt.ylabel("Sugar")
plt.show()

# BMI vs BP
plt.figure()
plt.scatter(df["BMI"], df["BP"])
plt.title("BMI vs Blood Pressure")
plt.xlabel("BMI")
plt.ylabel("BP")
plt.show()

# Sugar Distribution (Histogram)
plt.figure()
plt.hist(df["Sugar"], bins=5)
plt.title("Sugar Level Distribution")
plt.xlabel("Sugar")
plt.ylabel("Frequency")
plt.show()

# BP Distribution
plt.figure()
plt.hist(df["BP"], bins=5)
plt.title("Blood Pressure Distribution")
plt.xlabel("BP")
plt.ylabel("Frequency")
plt.show()

#health risk prediction function
def health_risk(age, bmi, sugar, bp):
    if sugar > 180 or bp > 160:
        return "🔴 High Risk"
    elif sugar > 140 or bp > 140 or bmi > 30:
        return "🟠 Moderate Risk"
    else:
        return "🟢 Healthy"

#health prediction 
print("\n🧠 Health Predictions:\n")

for i in range(len(df)):
    result = health_risk(df["Age"][i], df["BMI"][i], df["Sugar"][i], df["BP"][i])
    print(f"Person {i+1}: {result}")
