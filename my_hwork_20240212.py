#
# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит
# всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
#
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()
#
# Примечания:
# 1. Статья про one hot вид
# 2. Формат сдачи: ссылка на свой репозиторий.
# 3. Загрузите задание на проверку до 12 февр., 13:00 +03:00 UTC
# ==============================================================================================

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
