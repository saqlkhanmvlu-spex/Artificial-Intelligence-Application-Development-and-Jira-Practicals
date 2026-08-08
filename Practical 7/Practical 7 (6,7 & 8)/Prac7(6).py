import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
data = pd.read_csv("iris.csv")
X = data[['SepalLengthCm']]
y = data[['SepalWidthCm']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
model = DecisionTreeRegressor()
model.fit(X_train, y_train)
print("Training Accuracy : ",model.score(X_train, y_train)*100)
print("Testing Accuracy : ",model.score(X_test, y_test)*100)
new_data = pd.DataFrame([[11]],columns=['SepalLengthCm'])
prediction = model.predict(new_data)
print("Predicted SepalWidthCm : ",prediction[0])
print("Saqlain Khan T013")
