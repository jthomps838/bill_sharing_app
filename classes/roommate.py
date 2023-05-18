class Rommate:
    """
    Any individual in your home that would be paying part of the bill
    """

    def __init__(self, name, days_in_house, roommates=None):
        self.name = name
        self.days_in_house = days_in_house
        self.roommates = roommates

        if roommates:
            self._set_init_roommates(roommates)

    def set_pay_amount(self, bill, days_in_period):
        return bill.amount * (self.days_in_house / days_in_period / self.people_in_house)

    def add_roommate(self, person):
        if self.roommates:
            self.roommates.append(person)
        else:
            self.roommates = [person]

    def subtract_roommate(self, person):
        if self.roommates and person in self.roommates:
            self.roommates.remove(person)
        if person.roommates and self in person.roommates:
            person.roommates.remove(self)

    def _set_init_roommates(self, roommates):
        for roommate in roommates:
            if roommate.roommates and not self in roommate.roommates:
                roommate.add_roommate(self)
            else:
                self.roommates = [roommate]
                roommate.add_roommate(self)
