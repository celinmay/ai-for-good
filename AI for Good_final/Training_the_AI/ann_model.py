# Load model
from tensorflow import keras 
import pandas as pd 
import numpy as np
from sklearn.preprocessing import LabelEncoder

loaded_ann = keras.models.load_model('Covid_model')


# INPUT DATA START_____________________________________________________________
# Data to test 
data_test = pd.read_csv('symptom_frequency_test.csv')
X = data_test.iloc[:,:20].values

# Encoding it
le = LabelEncoder()
i = 0

# X's
for i in range(20):
    X[:,i] = le.fit_transform(X[:,i])
    i += 1
    
# Changing type 
X = np.array([X], dtype = np.float64)
X = X[-1, :]
    
# INPUT DATA FINISHED__________________________________________________________

# Trying it out
y_pred = loaded_ann.predict(X)

