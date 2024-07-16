import csv #we first import csv
class Item:
    pay_rate = 0.8
    all_items = []
    def __init__(self, name: str, price: int, quantity=0):
        #validate values
        assert price >=0, f"Ensure {price} is above 0"
        assert quantity >=0, f"Ensure {quantity} is above 0"
        
        self.name = name
        self.price = price
        self.quantity = quantity
        #append self
        Item.all_items.append(self)
    def calculate_total_price(self):
        return self.price * self.quantity
        
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    @classmethod
    def instantiate_from_csv(cls):
        with open('OOP/Advanced OOP Concepts/lesson3.csv', 'r') as f: #we can use with
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            #print(item)
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=float(item.get('quantity')),
            )
    @staticmethod
    def is_integer(number):
        if isinstance(number,float):
            return number.is_integer() #returns true if float is an integer ignores numbers with 100.0 as being floats and instead integers
        elif isinstance(number, int):
            return True
        else:
            return False
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})" #makes the repr more dynamic.

class Phone(Item):
    def __init__(self, name: str, price: int, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity)
        assert broken_phones >=0, f"Number of broken phones {broken_phones} should be greater than 0"
        self.brokenphones = broken_phones

try:
       
    phone1 = Phone("Nokia", 10000, 6, 2)
    print(phone1.calculate_total_price())
    # phone1.broken_phones = 1
    phone2 = Phone("Motorolla", 20000, 8, 2)
    # phone2.broken_phones = 2
    print(Item.all_items)
    print(Phone.all_items)
except Exception as e:
    print (e)
else:
    print(True)