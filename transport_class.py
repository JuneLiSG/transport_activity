class Transport():

    def __init__(self):
        self._is_on = False
        self.has_engine = True
        self._mode = "land"
        self.steering_type = "wheel"
        self._speed = 0
        self.type = "transport"

    def set_is_on(self, ignite: bool):
        if type(ignite) is bool:
            if ignite:
                if self._is_on == True:
                    if self._speed > 0:
                        # you are trying to ignite when it is already ignited and in motion
                        print(f"Your {self.type} is already on and you are in motion, you cannot ignite again")
                    else:
                        # you are already ignited and trying to ignite again
                        print(f"Your {self.type} is already on, you can start moving now")
                else:
                    # you have successfully ignited
                    self._is_on = True
                    print(f"You have just turned your {self.type} on, you are now ready to start moving")
            else:
                # you are trying to turn off, but you are in motion
                if self._speed > 0:
                    print(f"You need to stop before you can turn your {self.type} off")
                else:
                    # you are not in motion and...
                    if self._is_on == True:
                        # you are on so you are able to turn off
                        self._is_on = False
                        print(f"You have just turned your {self.type} off, bye :(")
                    else:
                        # you are already off so message to say so
                        print(f"Your {self.type} is already off, you can get out now")
        else:
            print("Please put in a valid input, True to turn on, False to turn off")

    def get_is_on(self):
        print(self._is_on)

    def accelerate(self, puts_foot_down: bool): # setter for _speed
        if type(puts_foot_down) is bool:
            if puts_foot_down:
                if self._is_on == True:
                    self._in_motion = True
                    self._speed += 30
                    print(f"You are now going at {self._speed}mph")
                else:
                    print(f"Your {self.type} is not on")
            else:
                pass
        else:
            print("Please input True to put your foot down")

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
                    print(f"Your {self.type} is not on, it doesn't make sense to brake")
            else:
                pass
        else:
            print("Please input True to slam brakes")

    def get_speed(self):
        print(self._speed)

# transport = Transport()