class House:
    """
    House that roommates are living in
    """

    def __init__(self, address, city, zipcode, roommates=None, bills=None):
        self.address = address
        self.city = city
        self.zipcode = zipcode
        self.roommates = roommates or []
        self.bills = {
            'electric': None,
            'gas': None,
            'cable': None,
            'internet': None,
            'water': None,
            'waste': None,
            'rent': None
        }

        if bills:
            for bill in bills:
                self.set_bill(bill)

        self._set_init_roommates(roommates)

    def add_roommate(self, person):
        if self.roommates is not None and not person in self.roommates:
            self.roommates.append(person)

    def subtract_roommate(self, person):
        if self.roommates and person in self.roommates:
            self.roommates.remove(person)
        if person.roommates and self in person.roommates:
            person.roommates.remove(self)

    def get_roommates(self):
        return self.roommates

    def _set_init_roommates(self, roommates):
        if roommates:
            for person in roommates:
                if not self in person.roommates:
                    person.add_roommate(self)
                    self.add_roommate(person)

    def set_bill(self, bill):
        try:
            self.bills[bill.get('type')] = bill
        except:
            return

    def get_bills(self):
        return self.bills

    def get_bill(self, bill_name):
        try:
            return self.bills.get(bill_name)
        except:
            return f'{bill_name} does not exist for this property.'
