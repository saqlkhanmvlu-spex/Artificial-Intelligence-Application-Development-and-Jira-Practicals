from sklearn.datasets import load_digits
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
data = pd.read_csv("mnist_test.csv")
digits = load_digits()
X = digits.data
y = digits.target
y = (y == 0)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
model = LogisticRegression(max_iter = 1000)
model.fit(X_train, y_train)
print("Training Accuracy : ", model.score(X_train, y_train)*100)
print("Testing Accuracy : ", model.score(X_test, y_test)*100)
prediction = model.predict([X_test[0]])
if prediction[0]:
  print("Digit is 0")
else:
  print("Digit is not 0")
print("Saqlain Khan T013")
