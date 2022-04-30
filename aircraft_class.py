from transport_class import Transport

class Aircraft(Transport):

    def __init__(self, name, passengers: int, max_speed: int, max_altitude: int):
        super().__init__()
        self.name = name
        self._passengers = passengers
        self._max_speed = max_speed
        self.type = "aircraft"
        self._max_altitude = max_altitude
        self._altitude = 0

    def accelerate(self, puts_foot_down: bool): # setter for _speed
        if type(puts_foot_down) is bool:
            if puts_foot_down:
                if self._is_on == True:
                    if self._speed + 30 <= self._max_speed:
                        self._speed += 30
                        print(f"You are now going at {self._speed} knots")
                    elif self._speed == self._max_speed:
                        print("You are already at your max speed, you cannot accelerate any more")
                    elif self._speed + 30 > self._max_speed:
                        self._speed = self._max_speed
                        print(f"You have just accelerated to your max speed {self._max_speed} knots")
                else:
                    print(f"Your {self.name} is not on")
            else:
                pass
        else:
            print("Please input True to put your foot down")

    def get_max_speed(self):
        print(f"Your max speed is {self._max_speed} knots")

    def get_passengers(self):
        print(f"Your {self.name} can carry {self._passengers} passengers.")

    def set_is_on(self, ignite: bool):
        if type(ignite) is bool:
            if self.has_engine == True:
                if ignite:
                    if self._is_on == True:
                        if self._speed > 0:
                            # you are trying to ignite when it is already ignited and in motion
                            print(f"Your {self.name} is already on and you are in motion, you cannot ignite again")
                        else:
                            # you are already ignited and trying to ignite again
                            print(f"Your {self.name} is already on, you can start moving now")
                    else:
                        # you have successfully ignited
                        self._is_on = True
                        print(f"You have just turned your {self.name} on, you are now ready to start moving")
                else:
                    # you are trying to turn off, but you are in motion
                    if self._speed > 0:
                        print(f"You need to stop before you can turn your {self.name} off")
                    elif self._altitude > 0:
                        print(f"You need to land before you can turn off your {self.name}")
                    else:
                        # you are not in motion and...
                        if self._is_on == True:
                            # you are on so you are able to turn off
                            self._is_on = False
                            print(f"You have just turned your {self.name} off, bye :(")
                        else:
                            # you are already off so message to say so
                            print(f"Your {self.name} is already off, you can get out now")
            else:
                if ignite:
                    print(f"Your {self.name} does not need to be turned on as there is no engine, "
                          f"you are already ready to go :)")
                else:
                    print(f"You don't need to turn your {self.name} off as it does not have an engine")
        else:
            print("Please put in a valid input, True to turn on, False to turn off")

    def set_altitude(self, ascend: bool):
        if type(ascend) is bool:
            if ascend:
                if self._is_on == True:
                    if self._altitude + 2000 <= self._max_altitude:
                        self._altitude += 2000
                        print(f"You have just ascended to {self._altitude}ft")
                    elif self._altitude == self._max_altitude:
                        print("You are already at your altitude limit, you cannot go any higher")
                    elif self._altitude + 2000 > self._max_altitude:
                        self._altitude = self._max_altitude
                        print(f"You have just reached your altitude limit {self._max_altitude}ft")
                else:
                    print(f"You can't do this because your {self.name} is not on")
            else:
                if self._is_on == True:
                    if self._altitude - 2000 <= 0:
                        self._altitude = 0
                        print(f"You have just landed")
                    elif self._altitude - 2000 > 0:
                        self._altitude = self._max_altitude
                        print(f"You have just descended to {self._altitude}ft")
                else:
                    print("You can't do this")

    def get_altitude(self):
        print(f"You are at {self._altitude}ft")

# heli = Aircraft("helicopter", 7, 140, 12000)
# boeing_747 = Aircraft("Boeing 747", 150, 614, 35000)