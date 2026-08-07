import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
data = pd.read_csv("housing.csv")
data = pd.get_dummies(data, columns=["ocean_proximity"])
X = data.drop("median_house_value", axis=1)
y = data["median_house_value"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)
model = DecisionTreeRegressor(random_state=1)
model.fit(X_train, y_train)
print("Training Score :", model.score(X_train, y_train) * 100)
print("Testing Score :", model.score(X_test, y_test) * 100)
prediction = model.predict([X_test.iloc[0]])
print("Predicted House Value :", prediction[0])
print("Saqlain Khan TO13")
