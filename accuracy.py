# Importing necessary libraries
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Loading the dataset
data = pd.read_csv('diabetes_data_upload_clean.csv')

# Splitting the data into features and target variable
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Performing feature scaling on the training and testing sets
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Creating a Logistic Regression model and training it on the training set
lr = LogisticRegression(random_state=42)
lr.fit(X_train, y_train)

# Making predictions on the testing set
y_pred = lr.predict(X_test)

# Evaluating the performance of the model
accuracy = lr.score(X_test, y_test)
print("Accuracy:", accuracy*100)
