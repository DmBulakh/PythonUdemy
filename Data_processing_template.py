# Importing libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer

# Importing dataset. Change the index and the name
data = pd.read_csv("Data.csv")
X = data.iloc[:, :-1].values
Y = data.iloc[:, 3].values


# Missing data
imputer = SimpleImputer(missing_values=np.nan, strategy="mean", verbose=0)
X[:, 1:3] = imputer.fit_transform(X[:, 1:3])

# Splitting the dataset into the Training and Test set
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

print(Y_train)

# Feature scaling
"""sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)  # when applying to the training set - fit to the tr. set and then transform the training set
X_test = sc_X.transform(X_train)  # already fitted
# Do we need to scale demi variables? As for me, no. We are losing he context
print(X_train)"""


