class Airport:
    # Define constructor
    def __init__(self):
        self._name = ""
        self.flights = []
        self.max_flights = 0

    # Define getter for name
    @property
    def name(self):
        return self._name

    # Define setter for name
    @name.setter
    def name(self, val):
        self._name = val

    # Define deleter for name
    @name.deleter
    def name(self):
        del self._name

