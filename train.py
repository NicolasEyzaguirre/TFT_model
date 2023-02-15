from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import pandas as pd
import pickle
def modelado(modelo=0):
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

    if modelo==0:
            logModel=LogisticRegression(C=0.08858667904100823,
                            solver='newton-cg',
                            max_iter=1000)
            logModel.fit(X_train, y_train)
            with open('model/model_23_02_14','wb') as archivo_salida:
                pickle.dump(logModel,archivo_salida)
            predictions_log2=logModel.predict(X_test)
            return accuracy_score(y_test, predictions_log2)

