class Bill:
    """
    Object that contains data about a bill,
    such as total amount of rent due per month
    """

    def __init__(self, bill, period, home=None):
        self.bill_name = bill.get('bill_name', 'No name')
        self.total_amount = bill.get('total_amount', 0)
        self.period = period
        self.taxes = bill.get('taxes')
        self.pre_tax_amount = bill.get('pre_tax_amount', 0)

        if home and bill:
            home.set_bill(bill)
