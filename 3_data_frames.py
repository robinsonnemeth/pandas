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
    '2nd quarter grade': [1,5,6.5,8.9,8],
    '3rd quarter grade': [3.5,8,'',5,9],
    '4th quarter grade': [4.2,8.5,5.9,8,9.5],
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

df = pd.DataFrame(report, columns=['Students','1st quarter grade','2nd quarter grade','3rd quarter grade','4th quarter grade','Average','Result'])
print(df)

exercise(4)
report = [
    {'Students':'Jhon Smith','1st quarter grade':5.4,'2nd quarter grade':1,'3rd quarter grade':3.5,'4th quarter grade':4.2,'Average':1,'Result':'Reprobate'},
    {'Students':'Andre Gonzales','1st quarter grade':6.2,'2nd quarter grade':5,'3rd quarter grade':8,'4th quarter grade':8.5,'Average':6.5,'Result':'Reprobate'},
    {'Students':'Juan Carlos Lima','1st quarter grade':8,'2nd quarter grade':6.5,'3rd quarter grade':'','4th quarter grade':5.9,'Average':8,'Result':'Approved'},
    {'Students':'Ann Robinson','1st quarter grade':8.5,'2nd quarter grade':8.9,'3rd quarter grade':5,'4th quarter grade':8,'Average':6.5,'Result':'Approved'},
    {'Students':'Thiago Pines','1st quarter grade':10,'2nd quarter grade':8,'3rd quarter grade':9,'4th quarter grade':9.5,'Average':9,'Result':'Approved'}
]
df = pd.DataFrame(report)
print(df)

exercise(5)
def convert_result_cell(cell):
    if cell=="Reprobate":
        return 'Review lesson'
    return cell
df = pd.read_excel('report.xlsx','Sheet1', converters = {
        'Result' : convert_result_cell
    })
print(df)

exercise(6)
#To create a new excel file
df.to_excel("new_file.xlsx", sheet_name="class")
new_df = pd.read_excel('new_file.xlsx','class')
print(new_df)

exercise(7)
df.to_excel("start_definition.xlsx", sheet_name="class", startrow=2, startcol=3, index=False)
new_df = pd.read_excel('start_definition.xlsx','class')
print(new_df)

exercise(8)
#Using two dataframes
df_grade3 = pd.DataFrame({
    'Students': ['Jhon Smith','Andre Gonzales','Juan Carlos Lima','Ann Robinson','Thiago Pines'],
    '1st quarter grade': [5.4,6.2,8,8.5,10],
    '2nd quarter grade': [1,5,6.5,8.9,8],
    '3rd quarter grade': [3.5,8,'',5,9],
    '4th quarter grade': [4.2,8.5,5.9,8,9.5],
    'Average': [1,6.5,8,6.5,9],
    'Result': ['Reprobate','Reprobate','Approved','Approved','Approved']
    })
df_grade4 = pd.DataFrame({
    'Students': ['Steven Moutain','Chris Cole','Ivan Torres','Sam Dias','Rodrigo Peres'],
    '1st quarter grade': [2.9,6.2,8,8.5,9],
    '2nd quarter grade': [1.8,5,6.5,8.9,10],
    '3rd quarter grade': [1.5,8,'',5,9],
    '4th quarter grade': [5.2,8.5,5.9,8,9.7],
    'Average': [1.1,6.5,8,6.5,8.9],
    'Result': ['Reprobate','Reprobate','Approved','Approved','Approved']
    })
with pd.ExcelWriter('two_df.xlsx') as writer:
    df_grade3.to_excel(writer, sheet_name="grade3")
    df_grade4.to_excel(writer, sheet_name="grade4")
    
two_df = pd.read_excel('two_df.xlsx','grade3')
print(two_df)
two_df = pd.read_excel('two_df.xlsx','grade4')
print(two_df)
