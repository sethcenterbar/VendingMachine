class Soda:
    def __init__(self, price, name, plant, country):
        self.price = price
        self.name = name
        self.plant = plant
        self.country = country

    def describe(self):
        print(
            f"I'm a {self.name}\nI cost {self.price} cents\nI'm from {self.country}")
