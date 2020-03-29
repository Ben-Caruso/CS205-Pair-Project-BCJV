# Used for basic testing
from passenger import Passenger
from flight import Flight
from airport import Airport

def main():
    airport = Airport()
    print(airport)
    flight = Flight()
    print(flight)

    airport.add_flight(flight)
    print(airport)

    passenger = Passenger(flight)
    print(passenger)
    print(passenger.get_flight().get_flight_time())


main()