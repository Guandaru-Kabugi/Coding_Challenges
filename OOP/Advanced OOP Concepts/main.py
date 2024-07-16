from item import Item
from phone import Phone

try:
       
    # phone1 = Phone("Nokia", 10000, 6, 2)
    # print(phone1.calculate_total_price())
    # # phone1.broken_phones = 1
    # phone2 = Phone("Motorolla", 20000, 8, 2)
    # # phone2.broken_phones = 2
    # print(Item.all_items)
    # print(Phone.all_items)
    # Item.instantiate_from_csv()
    # print(Item.all_items)
    item1 = Item("Item1", 1000)
    # item1._name = "MyItem" #allows you to make changes to attribute
    item1.apply_increment(0.5)
    print(item1.price) #although this is a function, we do not add parenthesis when calling. It acts like an attribute
    item1.apply_discount()
    print(item1.price)
except Exception as e:
    print (e)
else:
    print(True)