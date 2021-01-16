# Import libraries 
from tensorflow import keras 
import pandas as pd 
import numpy as np

# Import model 
loaded_ann = keras.models.load_model('Covid_model')

# Load data from CSV 
data_test = pd.read_csv('symptom_frequency.csv')
X = data_test.iloc[:,:20].values

# Predicting 
y_pred = loaded_ann.predict(X)

