import pandas as pd

report = pd.read_csv('C:\\Users\\carol\\Documents\\pandas\\report.csv')

def exercise(num):
    print(20*('*'))
    print(f'Exercise {num}: ')

exercise(1)
print(report)

exercise(2)
print(report['Average'])

exercise(3)
print(report['Average'].max())

exercise(4)
print(report['Average'].min())

exercise(5)
print(report['Students'][report['Result']=='Approved'])

exercise(6)
print(report['4st quarter grade'].mean())

exercise(7)
print(report['3st quarter grade'])
report.fillna(0, inplace=True)
print(report['3st quarter grade'])


