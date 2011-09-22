import xlrd, sys
import MySQLdb

sh = xlrd.open_workbook(sys.argv[1])
sheet = sh.sheet_by_index(0)
db = MySQLdb.connect(user="root",passwd="12345",db="ITC")
c = db.cursor()
for rownum in range(1,sheet.nrows):
    c.execute(""" INSERT INTO IP_cases_district_courts_and_judges VALUES
               (%s %s %s %s %s %s %s %s %s %s %s %s) """ %(row_values(rownum)[0],row_values(rownum)[1],row_values(rownum)[2],row_values(rownum)[3],
                                                           row_values(rownum)[4],row_values(rownum)[5],row_values(rownum)[6],
                                                           row_values(rownum)[7],row_values(rownum)[8],row_values(rownum)[9],
                                                           row_values(rownum)[10],row_values(rownum)[11]))

    
