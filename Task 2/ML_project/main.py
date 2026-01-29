from models.classification import *
from models.regression import *
from utils.metrics import *
# Linear Regression Model
reg = LinearRegression()
reg.fit()
reg.predict()
print("*" * 100)

# K-Nearest Neighbors Model
knn = KNNModel()
knn.predict()
knn.train()
print("*" * 100)

# Using metrics
score = accuracy_score()