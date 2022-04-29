from transport_class import Transport

class Car(Transport):

    def __init__(self, brand, colour, max_speed):
        super().__init__()
        self.brand = brand
        self.colour = colour
        self.max_speed = max_speed
        self.type = "car"

    def intro(self):
        print(f"I am a {self.brand} and I am {self.colour}, my max speed is {self.max_speed}mph."
              f"\nI travel on {self._mode}.")

my_car = Car("VW", "blue", 150)

my_car.intro()