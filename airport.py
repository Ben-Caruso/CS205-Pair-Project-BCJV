class Airport:
    # Define constructor
    def __init__(self):
        self.name = "Airport X"
        self.flights = []
        self.max_flights = 0

    # Define getter for name
    def get_name(self):
        return self.name

    # Define getter for flights
    def get_flights(self):
        return self.flights

    # Define getter for max_flights
    def get_max_flights(self):
        return self.max_flights

    # Define setter for name
    def set_name(self, new_name):
        self.name = new_name

    # Define setter for flights
    def set_flights(self, new_flights):
        self.flights = new_flights

    # Define setter for max flights
    def set_max_flights(self, new_max_flights):
        if new_max_flights < 0:
            self.max_flights = 0
        else:
            self.max_flights = new_max_flights

    # Define method to add a flight to the list
    def add_flight(self, flight):
        self.flights.append(flight)

    # Define method to remove a flight from the list
    def cancel_flight(self, flight):
        self.flights.remove(flight)

    # Define to_string method
    def __str__(self):
        s = self.name + ":"
        for i in self.flights:
            if i != len(self.flights):
                s += i.current_airport.name + " -> " + i.destination_airport.name \
                    + " at " + i.flight_time + " on " + i.flight_date + ","
            else:
                s += i.current_airport.name + " -> " + i.destination_airport.name \
                    + " at " + i.flight_time + " on " + i.flight_date
        if len(self.flights) == 0:
            s += " No flights right now"
        return s