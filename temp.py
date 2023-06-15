import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame(lst, columns=['whoAmI'])
print(data.head(5))
# print(pd.get_dummies(data.head(3)['whoAmI']))
data_wh =