from item import Item
class Phone(Item):
    def __init__(self, name: str, price: int, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity)
        assert broken_phones >=0, f"Number of broken phones {broken_phones} should be greater than 0"
        self.brokenphones = broken_phones