import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
data = pd.read_csv("student_marks.csv")
X = data[['Hours']]
y = data['Marks']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
model = LinearRegression()
model.fit(X_train, y_train)
print("Training Accuracy : ",
round(model.score(X_train, y_train) * 100, 2))
print("Testing Accuracy : ",
round(model.score(X_test, y_test) * 100, 2))
new_data = pd.DataFrame([[11]],columns=['Hours'])
pred = model.predict(new_data)
print("Predicted Marks for 11 Hours : ",round(pred[0],2))
print("Saqlain Khan T013")
