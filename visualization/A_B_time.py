import xlrd
import xlwt
book_trips = xlrd.open_workbook('dataFolder/trips.xls')
sheet_trips = book_trips.sheets()[0]

