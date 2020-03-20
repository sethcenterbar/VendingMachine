from soda import Soda

class SodaMachine:
    def __init__(self):
        self.change = 1500
        self.inventory = {}

    def load_machine(self):
        self.inventory = {
            "A1": {
                "count": 5,
                "item": Soda(100, "Coca Cola", "REEEE", "USA")
            },
            "A2": {
                "count": 4,
                "item": Soda(125, "Mountain Dew", "ARGGGG", "Denmark")
            },
            "B1": {
                "count": 5,
                "item": Soda(100, "Dr Pepper", "XXXX", "USA")
            },
            "B2": {
                "count": 4,
                "item": Soda(125, "Orange Soda", "ZZZZ", "Greenland")
            },
        }

    def add_inventory(self, key, soda, count):
        self.inventory[key] = {
            "count": count,
            "item": soda
        }

    def increment_selection(self, key):
        self.inventory[key]['count'] += 1

    def decrement_selection(self, key):
        self.inventory[key]['count'] -= 1

    def vend_by_key(self, key, inserted_money):
        count = self.inventory[key]['count']
        item = self.inventory[key]['item']
        price = self.inventory[key]['item'].price

        if count > 0:
            if inserted_money >= price:
                self.decrement_selection(key)
                return {
                    "item": item,
                    "change": inserted_money - price
                }
            else:
                print(f"You've inserted {inserted_money}, but the price is {price}!")
        else:
            print('Out of stock!')

    def describe_items(self):
        for item in self.inventory.values():
            print(item['item'].name)
