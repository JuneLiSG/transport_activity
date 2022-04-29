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

































        # self._doors_open = False

    # setter to set _is_on, check for valid boolean input
    # def ignite(self, turn_on:bool):
    #     if type(turn_on) != bool:
    #         print("Please input True to turn on, or False to turn off")
    #     elif turn_on == True:
    #         if self._is_on == True:
    #             print("Your transport is already on")
    #         else:
    #             self._is_on = True
    #             print("You have just turned your transport on - you are ready to go :)")
    #     else:
    #         if self._is_on == True:
    #             self._is_on = False
    #             print("You have just turned your transport off, bye :(")
    #         else:
    #             print("Your transport is already off, you can get out now :)")
    #
    # # setter for _in_motion
    # def move(self):
    #
    #     if self._is_on == True:
    #         return print("You are now on the move")
    #     else:
    #         return print("You need to turn your transport on before you can move")
    #
    # def stop(self):
    #     pass

    # setter for _doors_open, check for valid boolean input and other requirements before you can open/close door
    # def open_doors(self, pull_handle: bool):
    #     if type(pull_handle) != bool:
    #         print("Please input True to open the doors, False to close the doors")
    #     elif pull_handle == True:
    #         if self._doors_open == True:
    #             return print("Your doors are already open")
    #         else:
    #             self._doors_open = True
    #             return print("You just opened your doors, you are now ready to go :)")
    #     else:
    #         if self._doors_open == False:
    #             print("Your doors are already closed")
    #         else:
    #             self._doors_open = False
    #             print("You have just closed your doors, bye :(")




# transport = Transport()
#
# transport.ignite("other")
# transport.ignite(False)
#
# transport.ignite(True)
# transport.ignite(True)
# transport.ignite(False)
#
# transport.move()
# transport.ignite(True)
# transport.move()