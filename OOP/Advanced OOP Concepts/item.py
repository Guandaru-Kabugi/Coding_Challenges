import csv #we first import csv
class Item:
    pay_rate = 0.8
    all_items = []
    def __init__(self, name: str, price: int, quantity=0):
        #validate values
        assert price >=0, f"Ensure {price} is above 0"
        assert quantity >=0, f"Ensure {quantity} is above 0"
        
        # self._name = name #single underscore alows you make make changes or prevent changes to attribute
        self.__name = name
        self.__price = price
        self.quantity = quantity
        #append self
        Item.all_items.append(self)
    @property
    def price (self):
        return self.__price
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
    def apply_increment(self, increment):
        self.__price = self.__price + self.__price * increment
    @property
    def name (self):
        return self.__name
    @name.setter
    def name (self, value):
        self.__name = value
    def calculate_total_price(self):
        return self.__price * self.quantity
        
    
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
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})" #makes the repr more dynamic.
    # @property
    # def read_only_name(self): #This acts as an attribute
    #     return "yes AA"