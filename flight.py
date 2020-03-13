from airport import Airport

class Flight:
    def __init__(self):
        self.flight_number = 1111
        self.airline = ""

        self.passengers = []
        self.max_capacity = 0

        self.current_airport = Airport()
        self.destination_airport = Airport()
        self.flight_date = ""
        self.flight_time = ""
