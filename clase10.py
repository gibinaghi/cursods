import numpy as np
import pandas as pd
'''#  creo el data frame
data = np.array([['', 'Col1', 'Col2'], ['Fila1', 11, 22], ['Fila2', 33, 44]])
#  imprimo el data frame
print(pd.DataFrame(data=data[1:, 1:], index=data[1:, 0], columns=data[0, 1:]))

df = pd.DataFrame(np.array([[1, 2, 3], [8, 9, 6]]))
print('DataFrame:')
print(df)

#  creo serie from scratch
serie = pd.Series(np.array([1, 2, 3, 5, 4]))
print('Serie:')
print(serie)'''

df = pd.read_csv('titanic3.csv')
# print(df)
print(df.head())
print()
print(df.head(1))
print()
print(df.isnull())
print()
print(df.describe())
print()
