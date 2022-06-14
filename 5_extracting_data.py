import pandas as pd

def exercise(num):
    print(20*('*'))
    print(f'Exercise {num}: ')

df = pd.read_csv("report.csv")

exercise(1)
g = df.groupby('Result')
for result in g:
    print(result)

exercise(2)
print(g.get_group('Approved'))

exercise(3)
print(df.max())

exercise(4)
# Each group
print(g.max())

exercise(5)
print(g.describe())


