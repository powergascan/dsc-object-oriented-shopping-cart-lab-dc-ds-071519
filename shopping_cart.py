class ShoppingCart(object):
    def __init__(self, total=0,employee_discount=None, items=[]):
        self.total=total
        self.employee_discount=employee_discount
        self.items=items
        