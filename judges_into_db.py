import xlrd, sys
import MySQLdb

sh = xlrd.open_workbook(sys.argv[1])
sheet = sh.sheet_by_index(0)
db = MySQLdb.connect(user="root",passwd="12345",db="ITC")
c = db.cursor()
for rownum in range(1,sheet.nrows):
    c.execute(""" INSERT INTO `ITC`.`IP_cases_district_courts_and_judges` (`id`, `judge_first_name`, `judge_middle_name`, `judge_last_name`, `birth_year`, `court_name`, `president_name`, `part_affliation_of_president`, `ABA_rating`, `senate_vote_date`, `commission_date`, `retirement`, `termination_date`) VALUES 
               (%d,'%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s') """ %(rownum,sheet.row_values(rownum)[0],sheet.row_values(rownum)[1],sheet.row_values(rownum)[2],sheet.row_values(rownum)[3],sheet.row_values(rownum)[4],sheet.row_values(rownum)[5],sheet.row_values(rownum)[6],sheet.row_values(rownum)[7],sheet.row_values(rownum)[8],sheet.row_values(rownum)[9],sheet.row_values(rownum)[10],sheet.row_values(rownum)[11]))

    
