import xlrd
book = xlrd.open_workbook('station2.xls')
# 获取表名
names = book.sheet_names()
print(names)
sheet = book.sheets()[0]

