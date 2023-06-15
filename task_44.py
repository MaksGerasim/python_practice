# В ячейке ниже представлен код генерирующий DataFrame,
# которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид.
# Сможете ли вы это сделать без get_dummies?
import random
import pandas as pd
import numpy as np

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data_oh = pd.DataFrame(lst, columns=['whoAmI'])
print(data_oh.head(5))
data_oh['human'] = np.where(data_oh['whoAmI'] == 'human', '1', '0')
data_oh['robot'] = np.where(data_oh['whoAmI'] == 'robot', '1', '0')
print(data_oh[['human', 'robot']].head(5))
