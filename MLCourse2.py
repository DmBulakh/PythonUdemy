# Importing libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression

# Importing dataset
data = pd.read_csv("Salary_Data.csv")
X = data.iloc[:, :-1].values
Y = data.iloc[:, 1].values
print(X, Y)
#
# # Missing data
# imputer = SimpleImputer(missing_values=np.nan, strategy="mean", verbose=0)
# X[:, 1:3] = imputer.fit_transform(X[:, 1:2])
#
# # Encoding categorical data
# labelencoder_X = LabelEncoder()
# transformer = ColumnTransformer([('one_hot_encoder', OneHotEncoder(), [0])], remainder='passthrough')
# X = np.array(transformer.fit_transform(X), dtype=np.float)
# labelencoder_Y = LabelEncoder()
# Y = labelencoder_Y.fit_transform(Y)
#
# Splitting the dataset into the Training and Test set
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=1/3, random_state=0)
#
print(X_train)

# # Feature scaling
# sc_X = StandardScaler()
# X_train = sc_X.fit_transform(X_train)  # when applying to the training set - fit to the tr. set and then transform the training set
# X_test = sc_X.transform(X_train)  # already fitted
# # Do we need to scale demi variables? As for me, no. We are losing he context
# print(X_train)

# Fitting SLR to the training set
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

# Predicting the Test set results
Y_pred = regressor.predict(X_test)
print(Y_pred)
print(Y_test)

# Visualising the Training set results
plt.scatter(X_train, Y_train, color = 'red')
plt.scatter(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Exp (Training Set)')
plt.xlabel('Years of Exp')
plt.ylabel('Salary')
plt.show()