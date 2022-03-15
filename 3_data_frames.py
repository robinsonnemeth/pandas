import pandas as pd

#Need install openpyxl with 'pip install openpyxl' command

def exercise(num):
    print(20*('*'))
    print(f'Exercise {num}: ')

exercise(1)
df = pd.read_excel('report.xlsx','Sheet1')
print(df)

exercise(2)
report = {
    'Students': ['Jhon Smith','Andre Gonzales','Juan Carlos Lima','Ann Robinson','Thiago Pines'],
    '1st quarter grade': [5.4,6.2,8,8.5,10],
    '2st quarter grade': [1,5,6.5,8.9,8],
    '3st quarter grade': [3.5,8,'',5,9],
    '4st quarter grade': [4.2,8.5,5.9,8,9.5],
    'Average': [1,6.5,8,6.5,9],
    'Result': ['Reprobate','Reprobate','Approved','Approved','Approved']
}

df = pd.DataFrame(report)
print(df)

exercise(3)
report = [
    ('Jhon Smith',5.4,1,3.5,4.2,1,'Reprobate'),
    ('Andre Gonzales',6.2,5,8,8.5,6.5,'Reprobate'),
    ('Juan Carlos Lima',8,6.5,'',5.9,8,'Approved'),
    ('Ann Robinson',8.5,8.9,5,8,6.5,'Approved'),
    ('Thiago Pines',10,8,9,9.5,9,'Approved')
]

df = pd.DataFrame(report, columns=['Students','1st quarter grade','2st quarter grade','3st quarter grade','4st quarter grade','Average','Result'])
print(df)

exercise(4)
report = [
    {'Students':'Jhon Smith','1st quarter grade':5.4,'2st quarter grade':1,'3st quarter grade':3.5,'4st quarter grade':4.2,'Average':1,'Result':'Reprobate'},
    {'Students':'Andre Gonzales','1st quarter grade':6.2,'2st quarter grade':5,'3st quarter grade':8,'4st quarter grade':8.5,'Average':6.5,'Result':'Reprobate'},
    {'Students':'Juan Carlos Lima','1st quarter grade':8,'2st quarter grade':6.5,'3st quarter grade':'','4st quarter grade':5.9,'Average':8,'Result':'Approved'},
    {'Students':'Ann Robinson','1st quarter grade':8.5,'2st quarter grade':8.9,'3st quarter grade':5,'4st quarter grade':8,'Average':6.5,'Result':'Approved'},
    {'Students':'Thiago Pines','1st quarter grade':10,'2st quarter grade':8,'3st quarter grade':9,'4st quarter grade':9.5,'Average':9,'Result':'Approved'}
]
df = pd.DataFrame(report)
print(df)
