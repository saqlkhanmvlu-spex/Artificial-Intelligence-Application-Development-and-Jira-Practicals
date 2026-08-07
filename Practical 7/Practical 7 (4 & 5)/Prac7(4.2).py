import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
data = pd.read_csv("housing.csv")
data = data.dropna()
data["ocean_proximity"] = data["ocean_proximity"].astype("category").cat.codes
X = data.drop("median_house_value", axis=1)
y = pd.qcut(data["median_house_value"], q=5, labels=False)
model = KNeighborsClassifier()
scores = cross_val_score(model, X, y, cv=5)
print("Accuracy scores for each fold :")
print(scores)
print("Average Accuracy :", round(scores.mean() * 100, 2), "%")
print("Saqlain Khan TO13")
