from classes.roommate import Rommate
from classes.bill import Bill
from classes.pdf_report import PdfReport

days_in_month = 30

joseph = Rommate(name='Joseph', days_in_house=30)
kim = Rommate(name="Kimberly", days_in_house=30, roommates=[joseph])

rent = Bill(bill={'total_amount': 1800, 'taxes': 21.09,
            'pre_tax_amount': 1789.91}, period='May 2023')

may_rent = PdfReport(filename='may_rent_2023')
