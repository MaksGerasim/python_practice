# Работать с файлом california_housing_train.csv, который находится в папке sample_data.
# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).
import numpy
import numpy as np
import pandas as pd


data = pd.read_csv('california_housing_test.csv')
print(numpy.mean(data.loc[data['population'] < 500, 'median_house_value'], axis=0))