from transport_class import Transport

class Boat():

    def __init__(self):
        super().__init__()
        self.has_sails = True
        self._mode = "Sea"
        self.type = "boat"
        self._is_docked = True

    def set_is_docked(self, ):