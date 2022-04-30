from transport_class import Transport


class Car(Transport):

    def __init__(self, brand, colour, max_speed: int):
        super().__init__()
        self.brand = brand
        self.colour = colour
        self.type = "car"
        self.max_speed = max_speed

    def intro(self):
        print(f"I am a {self.brand} and I am {self.colour}, my max speed is {self.max_speed}mph."
              f"\nI travel on {self._mode}.")

    def accelerate(self, puts_foot_down: bool): # setter for _speed
        if type(puts_foot_down) is bool:
            if puts_foot_down:
                if self._is_on == True:
                    if self._speed + 30 <= self.max_speed:
                        self._speed += 30
                        print(f"You are now going at {self._speed}mph")
                    elif self._speed == self.max_speed:
                        print("You are already at your max speed, you cannot accelerate any more")
                    elif self.max_speed + 30 > self.max_speed:
                        self._speed = self.max_speed
                        print(f"You have just accelerated to your max speed {self.max_speed}mph")
                else:
                    print(f"Your {self.type} is not on")
            else:
                pass
        else:
            print("Please input True to put your foot down")

    def get_max_speed(self):
        print(self.max_speed)


# my_car = Car("VW", "blue", 150)