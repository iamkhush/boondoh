import xlrd, sys
import MySQLdb

sh = xlrd.open_workbook(sys.argv[1])
sheet = sh.sheet_by_index(0)
db = MySQLdb.connect(user="root",passwd="12345",db="ITC")
c = db.cursor()
for rownum in range(1,sheet.nrows):
    c.execute(""" INSERT INTO `ITC`.`IP_cases_itc_cases` (`id`, `invoice_number`, `matter`, `unfair_acts_in_notice`, `patent_numbers`, `country`, `complainants`, `respondants`, `alj`, `oui_attorney`, `gc_attorney`, `status`, `notice`, `type`, `phase`, `inv_term_date`, `publ_comm_options`, `rel_court_decisions`, `status_results`, `dispos`, `unfair_acts`, `notes_ris_rem`, `act_exp_rem_orders`, `exclusion`, `target_date`, `violation_final_due_date`, `beg_end_dates_of_hearing`) VALUES 
               (%d,'%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s', '%s') """ %(rownum,sheet.row_values(rownum)[0],sheet.row_values(rownum)[1],sheet.row_values(rownum)[2],sheet.row_values(rownum)[3],sheet.row_values(rownum)[4],sheet.row_values(rownum)[5],sheet.row_values(rownum)[6],sheet.row_values(rownum)[7],sheet.row_values(rownum)[8],sheet.row_values(rownum)[9],sheet.row_values(rownum)[10],sheet.row_values(rownum)[11],sheet.row_values(rownum)[12],sheet.row_values(rownum)[13],sheet.row_values(rownum)[14],sheet.row_values(rownum)[15],sheet.row_values(rownum)[16],sheet.row_values(rownum)[17],sheet.row_values(rownum)[18],sheet.row_values(rownum)[19],sheet.row_values(rownum)[20],sheet.row_values(rownum)[21],sheet.row_values(rownum)[22],sheet.row_values(rownum)[23],sheet.row_values(rownum)[24],sheet.row_values(rownum)[25],sheet.row_values(rownum)[26]))

    