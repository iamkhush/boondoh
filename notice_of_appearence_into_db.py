import xlrd, sys
import MySQLdb

sh = xlrd.open_workbook(sys.argv[1])
sheet = sh.sheet_by_index(0)
db = MySQLdb.connect(user="root",passwd="12345",db="ITC")
c = db.cursor()
for rownum in range(25,sheet.nrows):
    print rownum              
    c.execute(""" INSERT INTO `ITC`.`IP_cases_n` (`id`, `doc_id`, `invoice_number`, `sec`, `F`, `offcial_recieve`, `firm__or_organisation`, `filled_on_behalf`, `office`, `state`, `attorney_first_name`, `attorney_last_name`, `notes`) VALUES 
               (%d,'%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s') """ %(rownum,sheet.row_values(rownum)[1],sheet.row_values(rownum)[2],sheet.row_values(rownum)[3],sheet.row_values(rownum)[4],sheet.row_values(rownum)[5],sheet.row_values(rownum)[6],sheet.row_values(rownum)[7],sheet.row_values(rownum)[8],sheet.row_values(rownum)[9],sheet.row_values(rownum)[10],sheet.row_values(rownum)[11]))

    
