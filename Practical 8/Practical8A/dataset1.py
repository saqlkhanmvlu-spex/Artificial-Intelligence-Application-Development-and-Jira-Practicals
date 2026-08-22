import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. LOAD AND EXPLORE THE DATASET
# ==========================================

df = pd.read_csv("train.csv")

print("========== 1. LOAD AND EXPLORE DATASET ==========")
print(df.head())
print("\nShape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())


# ==========================================
# 2. CHECK DATA QUALITY
# ==========================================

print("\n========== 2. CHECK DATA QUALITY ==========")

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())


# ==========================================
# 3. IDENTIFY TARGET VARIABLE
# ==========================================

print("\n========== 3. TARGET VARIABLE ==========")

target = "Survived"

print("Target Variable:", target)
print("\nTarget Values:")
print(df[target].value_counts())


# ==========================================
# 4. ANALYZE CLASS DISTRIBUTION
# ==========================================

print("\n========== 4. CLASS DISTRIBUTION ==========")

print(df["Survived"].value_counts())

print("\nPercentage Distribution:")
print(df["Survived"].value_counts(normalize=True) * 100)


# ==========================================
# 5. VISUALIZE CLASS IMBALANCE
# ==========================================

plt.figure(figsize=(6, 4))

sns.countplot(data=df, x="Survived")

plt.title("Survival Class Distribution")
plt.xlabel("Survival")
plt.ylabel("Number of Passengers")
plt.xticks([0, 1], ["Did Not Survive", "Survived"])

plt.show()


# ==========================================
# 6. GENDER REPRESENTATION
# ==========================================

print("\n========== 6. GENDER REPRESENTATION ==========")

print(df["Sex"].value_counts())

plt.figure(figsize=(6, 4))

sns.countplot(data=df, x="Sex")

plt.title("Gender Representation")
plt.xlabel("Gender")
plt.ylabel("Number of Passengers")

plt.show()


# ==========================================
# 7. SURVIVAL BY GENDER
# ==========================================

print("\n========== 7. SURVIVAL BY GENDER ==========")

print(pd.crosstab(df["Sex"], df["Survived"]))

print("\nSurvival Rate by Gender:")
print(df.groupby("Sex")["Survived"].mean() * 100)

plt.figure(figsize=(6, 4))

sns.countplot(data=df, x="Sex", hue="Survived")

plt.title("Survival by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Passengers")

plt.show()


# ==========================================
# 8. PASSENGER CLASS REPRESENTATION
# ==========================================

print("\n========== 8. PASSENGER CLASS REPRESENTATION ==========")

print(df["Pclass"].value_counts().sort_index())

plt.figure(figsize=(6, 4))

sns.countplot(data=df, x="Pclass")

plt.title("Passenger Class Representation")
plt.xlabel("Passenger Class")
plt.ylabel("Number of Passengers")

plt.show()


# ==========================================
# 9. SURVIVAL BY PASSENGER CLASS
# ==========================================

print("\n========== 9. SURVIVAL BY PASSENGER CLASS ==========")

print(pd.crosstab(df["Pclass"], df["Survived"]))

print("\nSurvival Rate by Passenger Class:")
print(df.groupby("Pclass")["Survived"].mean() * 100)

plt.figure(figsize=(6, 4))

sns.countplot(data=df, x="Pclass", hue="Survived")

plt.title("Survival by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Number of Passengers")

plt.show()


# ==========================================
# 10. ANALYZE AGE GROUPS
# ==========================================

print("\n========== 10. AGE GROUPS ==========")

bins = [0, 12, 18, 35, 60, 100]
labels = ["Child", "Teen", "Adult", "Middle-aged", "Senior"]

df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=bins,
    labels=labels
)

print(df["AgeGroup"].value_counts().sort_index())

plt.figure(figsize=(7, 4))

sns.countplot(data=df, x="AgeGroup")

plt.title("Age Group Distribution")
plt.xlabel("Age Group")
plt.ylabel("Number of Passengers")
plt.xticks(rotation=20)

plt.show()


# ==========================================
# 11. SURVIVAL BY AGE GROUP
# ==========================================

print("\n========== 11. SURVIVAL BY AGE GROUP ==========")

print(pd.crosstab(df["AgeGroup"], df["Survived"]))

print("\nSurvival Rate by Age Group:")
print(df.groupby("AgeGroup", observed=True)["Survived"].mean() * 100)

plt.figure(figsize=(7, 4))

sns.countplot(data=df, x="AgeGroup", hue="Survived")

plt.title("Survival by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Passengers")
plt.xticks(rotation=20)

plt.show()


# ==========================================
# 12. IDENTIFY POSSIBLE BIAS
# ==========================================

print("\n========== 12. POSSIBLE BIAS ==========")

print("Gender Survival Rate:")
print(df.groupby("Sex")["Survived"].mean() * 100)

print("\nPassenger Class Survival Rate:")
print(df.groupby("Pclass")["Survived"].mean() * 100)

print("\nPossible Bias:")
print("- Gender differences in survival")
print("- Passenger class differences")
print("- Age differences")
print("- Missing values")
print("- Unequal representation of groups")


# ==========================================
# 13. IMPACT ON MACHINE LEARNING
# ==========================================

print("\n========== 13. IMPACT ON MACHINE LEARNING ==========")

print("""
1. Class imbalance may affect model performance.
2. Missing values can reduce prediction accuracy.
3. Gender and passenger class may strongly influence predictions.
4. The model may learn historical patterns and biases.
5. Accuracy alone may not be sufficient for evaluation.
""")


# ==========================================
# 14. SUGGESTED SOLUTIONS
# ==========================================

print("\n========== 14. SUGGESTED SOLUTIONS ==========")

print("""
1. Handle missing Age values.
2. Handle missing Embarked values.
3. Drop or transform Cabin because of many missing values.
4. Use stratified train-test splitting.
5. Use class weights if required.
6. Evaluate using Precision, Recall and F1-score.
7. Check model performance across different groups.
""")


# ==========================================
# 15. FINAL CONCLUSION
# ==========================================

print("\n========== 15. FINAL CONCLUSION ==========")

print("""
The Titanic dataset shows that survival was strongly related to
gender, passenger class and age. Female and first-class passengers
had higher survival rates, while male and third-class passengers
had lower survival rates.

The dataset also contains missing values and differences in group
representation. Therefore, proper data preprocessing, bias analysis
and suitable evaluation metrics are important before applying
machine learning.
""")
