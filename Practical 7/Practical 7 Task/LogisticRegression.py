import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
data = pd.read_csv("netflix_titles.csv")
data['type'] = le.fit_transform(data['type'])
X = data[['release_year']]
y = data['type']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
model = LogisticRegression()
model.fit(X_train, y_train)
print("Training Accuracy : ",model.score(X_train, y_train)*100)
print("Testing Accuracy : ",model.score(X_test, y_test)*100)
prediction = model.predict([X_test.iloc[0]])
print("Predicted Class : ",prediction[0])
print("Saqlain Khan T013")
