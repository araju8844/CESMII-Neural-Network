import pandas as pd
balanced = 1
bottomBound = 1999
txt = open("D:/Research PSU 2020/Shaft_vibration_data-Ankur_Verma/Balanced_shaft_MEMS/160_25Hz_10s.txt")
data = txt.read()
datalst = data.split("\n")
topBound = 7999
del datalst[topBound+1:]
del datalst[:bottomBound]
i = 0
while i < len(datalst):
    templst = datalst[i].split(",")
    if balanced == 0:
        del templst[:2]
    else:
        del templst[:2]
        del templst[1:4]
    for j in templst:
        if j != '':
            j = float(j)
    datalst[i] = templst
    i += 1
df = pd.DataFrame(datalst)
writer = pd.ExcelWriter(
    'D:/Research PSU 2020/Clean Balanced MEMS/160_25Hz_10s.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='newdata', index=False)
writer.save()
