from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from joblib import load
import pandas as pd
import os

curr_path = os.getcwd()
data_path = os.path.join(curr_path, 'data.csv')

data = pd.read_csv(data_path)
data = data.set_index('id')
x = data.loc[:, ['radius_mean','area_mean']]
y = data.loc[:, ['diagnosis']]
logic = lambda val: 1 if val=='M' else 0
y['diagnosis'] = [ logic(d) for d in y['diagnosis']]
xtrain,xtest,ytrain,ytest = train_test_split(x,y,random_state=42) 

model = load('model.joblib') 

# Evaluation section :
ypred = model.predict(xtest)

print(" *** Accuracy Score *** \n")
print(f"Accuracy : {round((accuracy_score(ytest, ypred) * 100), 2)} %\n")
print(" *** ---- ---- ---- *** \n\n")
print(" *** Classification Report *** ")
print(classification_report(ytest, ypred))
print(" *** ---- ---- ---- *** \n\n")
print(" *** Confusion Matrix *** \n")
print(f"{confusion_matrix(ytest, ypred)}\n")
print(" *** ---- ---- ---- *** ")


