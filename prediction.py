
import pandas as pd
import pickle


def prediction():
    with open('model/model_23_02_14','rb') as archivo_entrada:
        loaded_model=pickle.load(archivo_entrada)
    Data=pd.read_csv('Data/Test_clean.csv')
    X=Data.drop(['placement'], axis=1)
    pred_placements=loaded_model.predict(X)
    Data['pred_placements']=pred_placements
    Data.to_csv('Data/Pred_Test.csv') 