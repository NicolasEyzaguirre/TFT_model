from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from datetime import datetime
import pickle

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def modelado(modelo=0,grafico=0,show=False):
    Data=pd.read_csv('Data/Train_clean.csv')
    X = Data.drop(['placement'], axis=1)
    y = Data['placement']
    X_train, X_test, y_train, y_test = train_test_split(
                                        X,
                                        y,
                                        train_size   = 0.8,
                                        random_state = 34,
                                        shuffle      = True
                                    )
    logModel=LogisticRegression(C=0.08858667904100823,
                            solver='newton-cg',
                            max_iter=1000)
    logModel.fit(X_train, y_train)
    predictions_log2=logModel.predict(X_test)
    

    now = datetime.now()
    filename = 'modelo_' + now.strftime('%Y-%m-%d') + '.pkl'

    if modelo==1:
                     
        with open('model/'+filename,'wb') as archivo_salida:
            pickle.dump(logModel,archivo_salida)
    
    if grafico==1:

        print(accuracy_score(y_test, predictions_log2))
        c_mat = confusion_matrix(y_test,predictions_log2, normalize = 'true')
        sns.heatmap(c_mat, annot=True)

    if grafico==2:

        fpr, tpr, thresholds = roc_curve(y_test, predictions_log2)
        plt.plot(fpr,tpr)
        plt.xlabel("False positive rate")
        plt.ylabel("True positive rate")
    
    if grafico==3:

        precisions, recalls, thresholds = precision_recall_curve(y_test, predictions_log2)
        plt.plot(precisions, recalls)
        plt.xlabel("Precision")
        plt.ylabel("Recall")

    if show == True :
        x_data=pd.DataFrame(X_test)
        x_data['placements']=y_test
        x_data['pred_placement']=predictions_log2
        return x_data.head(8)