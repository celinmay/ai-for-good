# Load model
from tensorflow import keras 

loaded_ann = keras.models.load_model('Covid_model')

# Trying it out
y_pred = loaded_ann.predict(X_test)
y_pred = (y_pred > 0.5) # MAYBE LEAVE THIS PART OUT, SO WE GET PROBABILITIES 
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))


# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
