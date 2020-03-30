# Used for basic testing
from passenger import Passenger
from flight import Flight
from airport import Airport


def main():
    airport_names = ['JFK', 'LAX', 'ATL', 'DFW']

    airports = initialize_airports(airport_names)
    for i in range(len(airports)):
        airports[i].add_flight(Flight())

        flights = airports[i].get_flights()
        for flight in flights:
            flight.set_current_airport(airports[i])
            flight.set_destination_airport(
                airports[i+1] if i < len(airports)-1 else airports[0])

    print_data(airports)


def initialize_airports(airport_names):
    airports = []

    # create airport objects
    for i in range(len(airport_names)):
        airports.append(Airport())

    # add names to objects
    for airport in airports:
        airport.set_name(airport_names[0])
        airport_names.remove(airport_names[0])

    return airports


def print_data(airports):
    for airport in airports:
        for flight in airport.get_flights():
            print(flight)


main()
