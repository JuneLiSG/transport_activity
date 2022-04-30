from transport_class import Transport


class Engineless(Transport):

    def __init__(self, name, colour, max_speed: int):
        super().__init__()
        self.has_wheels = True
        self.steering_type = "handlebars"
        self.has_engine = False
        self.type = "engineless"
        self._is_on = True
        self.max_speed = max_speed
        self.colour = colour
        self.name = name

    def accelerate(self, pedal: bool): # setter for _speed
        if type(pedal) is bool:
            if pedal:
                if self._is_on == True:
                    if self._speed + 30 <= self.max_speed:
                        self._speed += 30
                        print(f"You are now going at {self._speed}mph")
                    elif self._speed == self.max_speed:
                        print("You are already at your max speed, you cannot go any faster")
                    elif self.max_speed + 30 > self.max_speed:
                        self._speed = self.max_speed
                        print(f"You have just pedalled to your max speed {self.max_speed}mph")
                else:
                    print(f"Your {self.type} is not on")
            else:
                pass
        else:
            print("Please input True to start pedalling")

    def get_max_speed(self):
        print(self.max_speed)


# bicycle = Engineless("bike", "red", 50)
# scooter = Engineless("scooter", "green", 15)