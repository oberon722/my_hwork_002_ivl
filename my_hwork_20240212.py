#

import pandas as pd
import random

# Создаем DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Получаем уникальные значения
unique_values = data['whoAmI'].unique()

# Создаем столбцы для каждого уникального значения
for value in unique_values:
    data[value] = (data['whoAmI'] == value).astype(int)

# Удаляем исходный столбец 'whoAmI'
data.drop(columns=['whoAmI'], inplace=True)

print(data.head())
