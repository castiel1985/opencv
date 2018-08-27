from sklearn import datasets
import numpy as np
from keras.layers import Dense
from keras.models import Sequential
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

datasets = datasets.load_boston()

x = datasets.data
Y = datasets.target

seed = 7
np.random.seed(seed)


def create_model(unit_list=[13], optimizer='adam', init='normal'):
    model = Sequential()
    units = unit_list[0]
    model.add(Dense(units=units, activation='relu', input_dim=13, kernel_initializer=init))
    # 开始构建隐藏层

    for units in unit_list[1:]:
        model.add(Dense(units=units, activation='relu', kernel_initializer=init))

    model.add(Dense(units=1, kernel_initializer=init))

    # 开始编译模型
    model.compile(loss='mean_squared_error', optimizer=optimizer)

    return model


model = KerasRegressor(build_fn=create_model, epochs=200, batch_size=5, verbose=0)

kfold = KFold(n_splits=10, shuffle=True, random_state=seed)
results = cross_val_score(model, x, Y, cv=kfold)
print('beaeline: %.2f (%.2f) mse' % (results.mean(), results.std()))
