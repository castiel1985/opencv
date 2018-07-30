from sklearn import datasets
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold

dataset = datasets.load_iris()

x = dataset.data
y = dataset.target

seed = 7
np.random.seed(seed)

def create_model(optimizer='adam', init='glorot_uniform'):
    #构建模型
    model = Sequential()
    model.add(Dense(units=4, activation='relu', input_dim=4,kernel_initializer=init))
    model.add(Dense(units=6, activation='relu', kernel_initializer=init))
    model.add(Dense(units=3, activation='softmax', kernel_initializer=init))
    #开始编译模型
    model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])
    
    return model

model = KerasClassifier(build_fn=create_model, epochs=200, batch_size=5, verbose=0)
kfold = KFold(n_splits=10, shuffle=True, random_state=seed)
results = cross_val_score(model, x,y,cv=kfold)

print('Accuracy: %.2f%% (%.2f)' % (results.mean()*100, results.std()))

