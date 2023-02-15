
import pandas as pd
import pickle
from datetime import datetime
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import seaborn as sns

now = datetime.now()
filename = 'modelo_' + now.strftime('%Y-%m-%d') + '.pkl'

def prediction(show=False, grafico=0):
    with open('model/'+filename,'rb') as archivo_entrada:
        loaded_model=pickle.load(archivo_entrada)
    Data=pd.read_csv('Data/Test_clean.csv')
    y=Data['placement']
    X=Data.drop(['placement'], axis=1)
    pred_placements=loaded_model.predict(X)
    Data['pred_placements']=pred_placements
    Data.to_csv('Data/Pred_Test.csv') 
    if show== True:
        Data.head(8)
    if grafico==1:

        print(accuracy_score(y, pred_placements))
        c_mat = confusion_matrix(y,pred_placements, normalize = 'true')
        sns.heatmap(c_mat, annot=True)