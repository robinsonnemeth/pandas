import pandas as pd
import numpy as np

def exercise(num):
    print(20*('*'))
    print(f'Exercise {num}: ')

exercise(1)
df = pd.DataFrame({
    'Students': ['Jhon Smith','Andre Gonzales','Juan Carlos Lima','Ann Robinson','Thiago Pines'],
    'Birth': ['22/7/2013','21/8/2013','1/1/2012','11/12/2013','2/5/2012'],
    '1st quarter grade': ['',6.2,8,8.5,'10A'],
    '2nd quarter grade': [1,'',6.5,8.9,8],
    '3rd quarter grade': [-555,-999,'',5,9],
    '4th quarter grade': [4.2,'',5.9,8,9.5],
    'Average': [-999,3.1,8,6.5,''],
    'Result': ['Reprobate','Reprobate','Approved','Approved','']
    })
print(df)
df.to_excel("dates.xlsx", sheet_name="Sheet1", index=False)
df = pd.read_excel('dates.xlsx', parse_dates=["Birth"])
print(df)

exercise(2)
#Fill empty cells
new_df = df.fillna(0)
print(new_df['1st quarter grade'])

exercise(3)
new_df = df.fillna({"1st quarter grade" : 0, "2nd quarter grade" : 0, "3rd quarter grade" : 0, "4th quarter grade" : 0, "Average" : "To review", "Result" : "To review"})
print(new_df)

exercise(4)
new_df = df.dropna()
print(new_df)

exercise(5)
start_date = '01-01-2013'
end_date = '07-31-2013'
mask = (df['Birth']>start_date) & (df['Birth']<=end_date)
new_df = df.loc[mask]
print(new_df)

exercise(6)
print(df["3rd quarter grade"])
new_df = df.replace(-999,np.NaN)
print(new_df["3rd quarter grade"])

exercise(7)
print(df["3rd quarter grade"])
new_df = df.replace([-999,-555],np.NaN)
print(new_df["3rd quarter grade"])

exercise(8)
print(df["3rd quarter grade"])
new_df = df.replace({
    -999: np.NaN,
    -555: 'Error 5'
    })
print(new_df["3rd quarter grade"])

exercise(9)
print(df)
new_df = df.replace({
    '3rd quarter grade':-999,
    '3rd quarter grade':-555,
    'Average':-999
    },np.NaN)
new_df = new_df.replace({
    'Average':np.NaN},'Review')
print(new_df)

exercise(10)
print(df["1st quarter grade"])
new_df = df.replace({
    '1st quarter grade': '[A-Za-z]'
    },'',regex=True)
print(new_df["1st quarter grade"])
