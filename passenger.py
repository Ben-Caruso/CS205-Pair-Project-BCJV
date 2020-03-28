from flight import Flight

class Passenger:
    # Define constructor
    def __init__(self):
        self.name = ""
        self.flight = Flight()

    # Define getters
    def get_name(self):
        return self.name

    def get_flight(self):
        return self.flight

    # Define setters
    def set_name(self, new_name):
        self.name = new_name

    def set_flight(self, new_flight):
        self.flight = new_flight