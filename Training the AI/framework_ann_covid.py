# Artificial Neural Network

# Importing the libraries
import numpy as np
import pandas as pd
import tensorflow as tf
tf.__version__

# Part 1 - Data Preprocessing

# Importing the dataset
dataset = pd.read_csv('symptom_frequency.csv') # Enter dataset (Not done)
X = dataset.iloc[:,:20].values # Explanatory variables (Not done)
y = dataset.iloc[:, -1].values # Response variable (Not done)
#print(X)
#print(y)

# ENCODING CATEGORICAL DATA
# Label Encoding to binary column
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
i = 0

for i in range(20):
    X[:,i] = le.fit_transform(X[:,i])
    i += 1

le_2 = LabelEncoder()

y[:] = le_2.fit_transform(y[:])

# TRANSFORMING TO INT64 and FLOAT64
# y = object -> y = int64
y = np.array([y], dtype = np.int64)
y = y[-1, :]

# X = object -> X = float64
X = np.array([X], dtype = np.float64)
X = X[-1, :]

# One Hot Encoding the categorical column with more than two categories
#from sklearn.compose import ColumnTransformer
#from sklearn.preprocessing import OneHotEncoder
#ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [])], remainder='passthrough') # Enter column of interest (Not done)
#X = np.array(ct.fit_transform(X))
#print(X)
# END OF CATEGORICAL DATA

# Feature Scaling
#from sklearn.preprocessing import StandardScaler
#sc = StandardScaler()
#X = sc.fit_transform(X)
#print(X)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# From Numpy array to Tensorflow tensor 

#X_train = tf.convert_to_tensor(X_train)
#X_test = tf.convert_to_tensor(X_test)

#y_train = tf.convert_to_tensor(y_train)
#y_test = tf.convert_to_tensor(y_test)

# Part 2 - Building the ANN

# Initializing the ANN
ann = tf.keras.models.Sequential()

# Adding the input layer and the first hidden layer
ann.add(tf.keras.layers.Dense(units=6, activation='relu'))

# Adding the second hidden layer
ann.add(tf.keras.layers.Dense(units=6, activation='relu'))

# Adding the output layer
ann.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

# Part 3 - Training the ANN

# Compiling the ANN
ann.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Training the ANN on the Training set
ann.fit(X_train, y_train, batch_size = 32, epochs = 10)

# Part 4 - Making the predictions and evaluating the model

# Predicting the Test set results
y_pred = ann.predict(X_test)
y_pred = (y_pred > 0.5)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)