class Transport():

    def __init__(self):
        self._is_on = False
        self.has_engine = True
        self._mode = "land"
        self.steering_type = "wheel"
        self._speed = 0
        self.name = "transport"

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
                    print(f"Your {self.name} does not need to be turned on as there is no engine, you are already ready to go :)")
                else:
                    print(f"You don't need to turn your {self.name} off as it does not have an engine")
        else:
            print("Please put in a valid input, True to turn on, False to turn off")

    def get_is_on(self):
        print(self._is_on)

    def brake(self, slams_brakes: bool):
        if type(slams_brakes) is bool:
            if slams_brakes:
                if self._is_on == True:
                    if 0 < self._speed < 30:
                        self._speed = 0
                        print("You have just braked and are now stationary")
                    elif self._speed == 0:
                        print("You are already stationary, you cannot brake more")
                    else:
                        self._speed -= 30
                        print(f"You have just decelerated to {self._speed}mph")
                else:
                    print(f"Your {self.name} is not on, it doesn't make sense to brake")
            else:
                pass
        else:
            print("Please input True to slam brakes")

    def get_speed(self):
        print(self._speed)


# transport = Transport(100)