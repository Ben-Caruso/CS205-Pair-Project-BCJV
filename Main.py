class Airport:

    def __init__(self):
        self.name = ""
        self.flights = []
        self.max_flights = 0


class Flight:

    def __init__(self):
        self.flight_number = 1111
        self.airline = ""

        self.passengers = []
        self.max_capacity = 0

        self.current_airport = ""
        self.destination_airport = ""
        self.flight_date = ""
        self.flight_time = ""


class Passenger:

    def __init__(self):
        self.name = ""
        self.flight = ""
