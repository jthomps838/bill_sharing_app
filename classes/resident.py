class Resident:
    """
    Any individual in your home that would be paying part of the bill
    """

    def __init__(self, name, home, roommates=None):
        self.name = name
        self.home = home

        self.home.add_roommate(self)

        if roommates:
            for person in roommates:
                self.home.add_roommate(person)

    def get_pay_amount(self, bill, ratio):
        return bill.amount * (ratio / len(self.home.roommates))
