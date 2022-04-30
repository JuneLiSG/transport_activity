from transport_class import Transport


class Boat(Transport):

    def __init__(self, colour, size, max_speed: int):
        super().__init__()
        self.has_sails = True
        self._mode = "Sea"
        self.type = "boat"
        self.max_speed = max_speed
        self.colour = colour
        self.size = size

    def accelerate(self, raise_sails: bool): # setter for _speed
        if type(raise_sails) is bool:
            if raise_sails:
                if self._is_on == True:
                    if self._speed + 30 <= self.max_speed:
                        self._speed += 30
                        print(f"You are now going at {self._speed} knots")
                    elif self._speed == self.max_speed:
                        print("You are already at your max speed, you cannot go any faster")
                    elif self.max_speed + 30 > self.max_speed:
                        self._speed = self.max_speed
                        print(f"You have just accelerated to your max speed {self.max_speed} knots")
                else:
                    print(f"Your {self.type} is not on")
            else:
                pass
        else:
            print("Please input True to put raise your sails")

    def brake(self, lower_sails: bool):
        if type(lower_sails) is bool:
            if lower_sails:
                if self._is_on == True:
                    if 0 < self._speed < 30:
                        self._speed = 0
                        print("You have just lowered your sails and are now stationary")
                    elif self._speed == 0:
                        print("You are already stationary, you cannot go any slower")
                    else:
                        self._speed -= 30
                        print(f"You have just decelerated to {self._speed} knots")
                else:
                    print(f"Your {self.type} is not on")
            else:
                pass
        else:
            print("Please input True to lower your sails")

    def get_max_speed(self):
        print(self.max_speed)

# my_boat = Boat("yellow", "medium", 200)
# print(my_boat.colour)