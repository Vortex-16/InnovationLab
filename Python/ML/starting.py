import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data = {
    "hours_studied": [1, 2, 3, 4, 5, 6, 7, 8],
    "passed": [0, 0, 0, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)
# print(df)

X = df[["hours_studied"]]  # input
y = df["passed"]          # output

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)

new_data = pd.DataFrame([[3.3]], columns=["hours_studied"]) #Enter Study time here
result = model.predict(new_data)

print("Pass" if result[0] == 1 else "Fail")