import pandas as pd

df = pd.read_csv('C:\\Users\\carol\\Documents\\pandas\\report.csv')

def exercise(num):
    print(20*('*'))
    print(f'Exercise {num}: ')

exercise(1)
rows, columns = df.shape
print(rows)
print(columns)

exercise(2)
print(df.columns)

exercise(3)
print(df.head)
print(df.head(3))

exercise(4)
print(df.tail(3))

exercise(5)
print(df[['Students', 'Result']])

exercise(6)
print(type(df['Average']))

exercise(7)
print(df.describe())

exercise(8)
print(df[df.Average==df['Average'].max()])

exercise(9)
print(df[['Students','Average']][df.Average>5])

exercise(10)
print(df.index)

exercise(11)
print(df.set_index('Students'))

exercise(12)
df.set_index('Students',inplace=True)
print(df.loc['Ann Robinson'])







