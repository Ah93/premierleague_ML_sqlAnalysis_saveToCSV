import pandas as pd
from sklearn.tree import DecisionTreeClassifier


pl_data = pd.read_csv("PL_Data.csv")
X = pl_data.drop(columns=["team"])
y = pl_data["team"]

pl_model = DecisionTreeClassifier()
pl_model.fit(X, y)
predictions = pl_model.predict([[23, 10, 5, 79, 37], [19, 6, 13, 63, 47]])
predictions