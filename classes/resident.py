from functools import reduce


class Resident:
    """
    Any individual in your home that would be paying part of the bill
    """

    def __init__(self, name, home, is_paying=False, roommates=None):
        self.name = name
        self.home = home
        self.is_paying = is_paying

        self.home.add_roommate(self)

        if roommates:
            for person in roommates:
                self.home.add_roommate(person)

    def get_pay_amount(self, bill, ratio):
        return '{:.2f}'.format(bill.total_amount * (ratio / len(self.home.get_paying_residents())))
