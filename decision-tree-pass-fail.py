Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import pandas as pd

... 
>>> from sklearn.linear_model import LogisticRegression

... from sklearn.model_selection import train_test_split
>>> from sklearn.model_selection import train_test_split
>>> from sklearn.metrics import accuracy_score
>>> data = {
...     "Hours_Studied": [1,2,3,4,5,6,7,8],
...     "Passed": [0,0,0,1,1,1,1,1]
...     }
>>> df = pd.DataFrame(data)
>>> X = df[["Hours_Studied"]]
>>> y = df["Passed"]
>>> X_train, X_test, y_train, y_test = train_test_split(
...     X, y, test_size=0.25, random_state=42
...     )
>>> model = LogisticRegression()
>>> model.fit(X_train, y_train)
LogisticRegression()
>>> y_pred = model.predict(X_test)
>>> print("Accuracy:", accuracy_score(y_test, y_pred))
Accuracy: 1.0
