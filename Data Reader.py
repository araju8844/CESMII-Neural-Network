import pandas as pd


def createExcelFile(topBound, bottomBound, textLoc, excelLoc, balanced):
    txt = open(textLoc)
    data = txt.read()
    datalst = data.split("\n")
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
        excelLoc, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='newdata', index=False)
    writer.save()
