from classes.resident import Resident
from classes.bill import Bill
from classes.pdf_report import PdfReport
from classes.home import House

# TEST HOME
home = House(address='123 Happy Road', city='Atlanta', zipcode='30075')

# TEST RESIDENTS
joseph = Resident(name='Joseph', home=home, is_paying=True)
kim = Resident(name="Kimberly", home=home, is_paying=True, roommates=[joseph])
parker = Resident(name='Parker', home=home)

print([roommate.name for roommate in home.get_roommates()])
# TEST BILL
rent = Bill(bill={'total_amount': 1800, 'taxes': 21.09,
            'pre_tax_amount': 1789.91, 'type': 'rent'}, period='May 2023', home=home)
electric = Bill(bill={'total_amount': 121.09, 'taxes': 21.09,
                      'pre_tax_amount': 100.00, 'type': 'electric'}, period='May 2023', home=home)

# TEST PDF REPORT
may_rent = PdfReport(filename='may_rent_2023')

print(home.get_bills())

print(joseph.get_pay_amount(rent, 1))
