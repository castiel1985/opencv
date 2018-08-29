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

steps = []
steps.append(('standarize', StandardScaler()))
steps.append(('mlp', model))

pipeline = Pipeline(steps)
kfold = KFold(n_splits=10, shuffle=True, random_state=seed)
results = cross_val_score(pipeline, x, Y, cv=kfold)
print('Standardize: %.2f (%.2f) mse' % (results.mean(), results.std()))

# 调参数选择最优模型

param_grid = {}
param_grid['units_list'] = [[20], [13, 6]]
param_grid['optimizer'] = ['rmsprop', 'adam']
param_grid['init'] = ['glorot_uniform', 'normal']
param_grid['epochs'] = [100, 200]
param_grid['batch_size'] = [5, 20]

scaler = StandardScaler()
scaler_x = scaler.fit_transform(x)
grid = GridSearchCV(estimator=model, param_grid=param_grid)
results = grid.fit(scaler_x, Y)

print('Best: %f using %s' % (results.best_score_, results.best_params_))
means = results.cv_results_['mean_test_score']
stds = results.cv_results_['std_test_score']
params = results.cv_results_['params']

for mean, std, param in zip(means, stds, params):
    print('%f (%f) with : %r' % (mean, std, param))
