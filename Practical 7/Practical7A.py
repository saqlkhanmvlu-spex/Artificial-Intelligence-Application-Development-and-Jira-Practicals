import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, StandardScaler

df = pd.read_csv("iris - iris - iris.csv")

print("\n========== 1. LOAD THE DATASET ==========")
print(df)
print("\nSaqlain Khan T013")

print("\n========== 2. DISPLAY THE DATASET ==========")
print(df)
print("\nSaqlain Khan T013")

print("\n========== 3. CHECK DATASET INFORMATION ==========")
df.info()
print("\nSaqlain Khan T013")

print("\n========== 4. DISPLAY DATASET SHAPE ==========")
print(df.shape)
print("\nSaqlain Khan T013")

print("\n========== 5. DISPLAY COLUMN NAMES ==========")
print(df.columns)
print("\nSaqlain Khan T013")

print("\n========== 6. DISPLAY SUMMARY STATISTICS ==========")
print(df.describe())
print("\nSaqlain Khan T013")

print("\n========== 7. CHECK DATA TYPES ==========")
print(df.dtypes)
print("\nSaqlain Khan T013")

print("\n========== 8. CHECK MISSING VALUES ==========")
print(df.isnull().sum())
print("\nSaqlain Khan T013")

print("\n========== 9. HANDLE MISSING VALUES ==========")
df.fillna(df.mean(numeric_only=True), inplace=True)
print(df.isnull().sum())
print("\nSaqlain Khan T013")

print("\n========== 10. REMOVE DUPLICATE RECORDS ==========")
df.drop_duplicates(inplace=True)
print(df)
print("\nSaqlain Khan T013")

print("\n========== 11. ENCODE CATEGORICAL DATA ==========")
encoder = LabelEncoder()
df["species"] = encoder.fit_transform(df["species"])
print(df)
print("\nSaqlain Khan T013")

print("\n========== 12. RENAME COLUMNS ==========")
df.rename(columns={
    "sepal_length": "Sepal_Length",
    "sepal_width": "Sepal_Width",
    "petal_length": "Petal_Length",
    "petal_width": "Petal_Width",
    "species": "Species"
}, inplace=True)
print(df)
print("\nSaqlain Khan T013")

print("\n========== 13. DROP UNNECESSARY COLUMNS ==========")
df.drop(columns=[], inplace=True)
print(df)
print("\nSaqlain Khan T013")

print("\n========== 14. SELECT FEATURES ==========")
X = df.drop("Species", axis=1)
print(X)
print("\nSaqlain Khan T013")

print("\n========== 15. CREATE NEW FEATURE ==========")
df["Total_Length"] = df["Sepal_Length"] + df["Petal_Length"]
print(df)
print("\nSaqlain Khan T013")

print("\n========== 16. CONVERT DATA TYPES ==========")
df["Species"] = df["Species"].astype(int)
print(df.dtypes)
print("\nSaqlain Khan T013")

print("\n========== 17. NORMALIZE DATA (MIN-MAX SCALING) ==========")
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(X)
print(normalized_data)
print("\nSaqlain Khan T013")

print("\n========== 18. STANDARDIZE DATA (STANDARD SCALING) ==========")
standard_scaler = StandardScaler()
standardized_data = standard_scaler.fit_transform(X)
print(standardized_data)
print("\nSaqlain Khan T013")

print("\n========== 19. SPLIT FEATURES AND TARGET VARIABLE ==========")
X = df.drop(["Species"], axis=1)
y = df["Species"]
print("Features (X):")
print(X)
print("\nTarget (y):")
print(y)
print("\nSaqlain Khan T013")
