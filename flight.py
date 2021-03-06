from airport import Airport


class Flight:

    # Define constructor
    def __init__(self):
        self.flight_number = 'Flight_number'
        self.airline = "Airline"

        self.passengers = []
        self.max_capacity = 0

        self.current_airport = Airport()
        self.destination_airport = Airport()
        self.flight_date = "flight_date"
        self.flight_time = "flight_time"

    @classmethod
    def airports_to_from(cls, current_airport, destination_airport):
        # Create flight with given information
        flight = Flight()
        flight.set_flight_number("Flight_Number")
        flight.set_airline("Airline")
        flight.set_passengers([])
        flight.set_max_capacity(0)
        flight.set_current_airport(current_airport)
        flight.set_destination_airport(destination_airport)
        flight.set_flight_date("Flight_Date")
        flight.set_flight_time("Flight_Time")
        return flight



    # Define getters
    def get_flight_number(self):
        return self.flight_number

    def get_airline(self):
        return self.airline

    def get_passengers(self):
        return self.passengers

    def get_max_capacity(self):
        return self.max_capacity

    def get_current_airport(self):
        return self.current_airport

    def get_destination_airport(self):
        return self.destination_airport

    def get_flight_date(self):
        return self.flight_date

    def get_flight_time(self):
        return self.flight_time

    # Define setters
    def set_flight_number(self, new_number):
        self.flight_number = new_number

    def set_airline(self, new_airline):
        self.airline = new_airline

    def set_passengers(self, new_passengers):
        self.passengers = new_passengers

    def set_max_capacity(self, new_max_capacity):
        self.max_capacity = new_max_capacity

    def set_current_airport(self, new_current_airport):
        self.current_airport = new_current_airport

    def set_destination_airport(self, new_destination_airport):
        self.destination_airport = new_destination_airport

    def set_flight_date(self, new_flight_date):
        self.flight_date = new_flight_date

    def set_flight_time(self, new_flight_time):
        self.flight_time = new_flight_time

    # Add/remove passenger from flight
    def add_passenger(self, passenger):
        self.passengers.append(passenger)
        passenger.set_flight(self)

    def remove_passenger(self, passenger):
        self.passengers.remove(passenger)

    # Define to_string method for flight
    def __str__(self):
        s = self.airline + " " + self.flight_number + ": " + self.current_airport.name + " -> " + self.destination_airport.name \
            + " at " + self.flight_time + " on "  + self.flight_date
        return s
