import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
data = pd.read_csv("iris.csv")
iris = load_iris()
X = iris.data
y = iris.target
model = KNeighborsClassifier()
scores = cross_val_score(model, X, y, cv=5)
print("Accuracy scores for each fold :")
print(scores)
print("Average Accuracy : ", round(scores.mean() * 100, 2), "%")
print("Saqlain Khan TO13")
