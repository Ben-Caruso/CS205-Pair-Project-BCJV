class Airport:
    # Define constructor
    def __init__(self):
        self.name = "Airport_Name"
        self.flights = []
        self.max_flights = 100

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
        # Validate that the airport has room for another flight and that the flight has this airport
        # as either a departure or destination location
        if len(self.flights) <= self.max_flights:
            self.flights.append(flight)
        else:
            print("Maximum capacity of flights reached: ", self.get_name())

    # Define method to remove a flight from the list
    def remove_flight(self, flight):
        # Remove flight from list
        self.flights.remove(flight)
        # For each passenger on this flight, set flight to None
        for p in flight.get_passengers():
            p.set_flight(None)

    def print_flight(self):
        for i in self.flights:
            print(i)

    # Get all incoming flights
    def get_incoming_flights(self):
        incoming = []
        for f in self.flights:
            if f.get_destination_airport() == self:
                incoming.append(f)
        return incoming

    # Get all outgoing flights
    def get_outgoing_flights(self):
        outgoing = []
        for f in self.flights:
            if f.get_current_airport() == self:
                outgoing.append(f)
        return outgoing

    # Define to_string method
    def __str__(self):
        s = self.name + ":"
        for i in self.flights:
            s += i.current_airport.name + " -> " + i.destination_airport.name \
                 + " at " + i.flight_time + " on " + i.flight_date
            if i != len(self.flights):
                s += ","
        if len(self.flights) == 0:
            s += " No flights right now"
        return s
