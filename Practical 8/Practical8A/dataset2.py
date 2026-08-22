import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. LOAD AND EXPLORE THE DATASET
# ==========================================

df = pd.read_csv("german_credit_data.csv")

print("========== 1. LOAD AND EXPLORE DATASET ==========")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

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

print("\nDuplicate Rows:")
print(df.duplicated().sum())


# ==========================================
# 3. IDENTIFY THE TARGET VARIABLE
# ==========================================

print("\n========== 3. IDENTIFY TARGET VARIABLE ==========")

possible_targets = ["Risk", "risk", "Credit Risk", "Class", "class"]

target = None

for col in possible_targets:
    if col in df.columns:
        target = col
        break

if target:
    print("Target Variable:", target)
else:
    print("Credit Risk target variable is NOT present in this dataset.")
    print("Available columns are:")
    print(df.columns.tolist())


# ==========================================
# 4. ANALYZE CLASS DISTRIBUTION
# ==========================================

print("\n========== 4. CLASS DISTRIBUTION ==========")

if target:
    print(df[target].value_counts())

    print("\nPercentage Distribution:")
    print(df[target].value_counts(normalize=True) * 100)

else:
    print("Cannot analyze credit-risk class distribution.")
    print("Reason: Target variable is missing.")


# ==========================================
# 5. VISUALIZE CLASS IMBALANCE
# ==========================================

print("\n========== 5. CLASS IMBALANCE ==========")

if target:

    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x=target)

    plt.title("Credit Risk Class Distribution")
    plt.xlabel("Credit Risk")
    plt.ylabel("Number of Customers")

    plt.show()

else:
    print("Cannot display credit-risk class imbalance.")
    print("Reason: Credit Risk target variable is missing.")


# ==========================================
# 6. GENDER REPRESENTATION
# ==========================================

print("\n========== 6. GENDER REPRESENTATION ==========")

print(df["Sex"].value_counts())

plt.figure(figsize=(6, 4))

sns.countplot(data=df, x="Sex")

plt.title("Gender Representation")
plt.xlabel("Gender")
plt.ylabel("Number of Customers")

plt.show()


# ==========================================
# 7. CREDIT RISK BY GENDER
# ==========================================

print("\n========== 7. CREDIT RISK BY GENDER ==========")

if target:

    print(pd.crosstab(df["Sex"], df[target]))

    plt.figure(figsize=(6, 4))

    sns.countplot(data=df, x="Sex", hue=target)

    plt.title("Credit Risk by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Number of Customers")

    plt.show()

else:
    print("Cannot analyze Credit Risk by Gender.")
    print("Reason: Credit Risk target variable is missing.")


# ==========================================
# 8. AGE GROUPS
# ==========================================

print("\n========== 8. AGE GROUPS ==========")

bins = [0, 18, 30, 45, 60, 100]

labels = [
    "18 or below",
    "19-30",
    "31-45",
    "46-60",
    "60+"
]

df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=bins,
    labels=labels
)

print(df["AgeGroup"].value_counts().sort_index())

plt.figure(figsize=(7, 4))

sns.countplot(
    data=df,
    x="AgeGroup",
    order=labels
)

plt.title("Age Group Distribution")
plt.xlabel("Age Group")
plt.ylabel("Number of Customers")

plt.xticks(rotation=20)

plt.show()


# ==========================================
# 9. CREDIT RISK BY AGE GROUP
# ==========================================

print("\n========== 9. CREDIT RISK BY AGE GROUP ==========")

if target:

    print(pd.crosstab(df["AgeGroup"], df[target]))

    plt.figure(figsize=(8, 4))

    sns.countplot(
        data=df,
        x="AgeGroup",
        hue=target,
        order=labels
    )

    plt.title("Credit Risk by Age Group")
    plt.xlabel("Age Group")
    plt.ylabel("Number of Customers")

    plt.xticks(rotation=20)

    plt.show()

else:
    print("Cannot analyze Credit Risk by Age Group.")
    print("Reason: Credit Risk target variable is missing.")


# ==========================================
# 10. HOUSING CATEGORY REPRESENTATION
# ==========================================

print("\n========== 10. HOUSING CATEGORY REPRESENTATION ==========")

print(df["Housing"].value_counts())

plt.figure(figsize=(6, 4))

sns.countplot(data=df, x="Housing")

plt.title("Housing Category Representation")
plt.xlabel("Housing Category")
plt.ylabel("Number of Customers")

plt.show()


# ==========================================
# 11. CREDIT RISK BY HOUSING CATEGORY
# ==========================================

print("\n========== 11. CREDIT RISK BY HOUSING CATEGORY ==========")

if target:

    print(pd.crosstab(df["Housing"], df[target]))

    plt.figure(figsize=(7, 4))

    sns.countplot(
        data=df,
        x="Housing",
        hue=target
    )

    plt.title("Credit Risk by Housing Category")
    plt.xlabel("Housing Category")
    plt.ylabel("Number of Customers")

    plt.show()

else:
    print("Cannot analyze Credit Risk by Housing Category.")
    print("Reason: Credit Risk target variable is missing.")


# ==========================================
# 12. IDENTIFY POSSIBLE BIAS
# ==========================================

print("\n========== 12. POSSIBLE BIAS ==========")

print("""
Possible sources of bias include:

1. Gender representation may be unequal.
2. Some age groups may have more customers than others.
3. Housing categories may not be equally represented.
4. Missing values may affect analysis.
5. If a Credit Risk target is added later, differences
   between demographic groups should be checked carefully.
""")
