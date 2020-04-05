# Used for basic testing
from passenger import Passenger
from flight import Flight
from airport import Airport

import pandas as pd
import numpy as np


def main():
    airport_names = ['JFK', 'LAX', 'ATL', 'DFW']
    # string flight_num, string airline, string date, string time
    flight_info = [["UA1215", "United Airlines", "3/20/2020", "3:30pm"],
                   ["UA1438", "United Airlines", "3/20/2020", "3:45pm"],
                   ["UA3455", "United Airlines", "3/20/2020", "4:00pm"],
                   ["UA4234", "United Airlines", "3/20/2020", "4:15pm"]]

    # read_csv of names
    df = pd.read_csv('baby_names.csv')
    # get name values
    names = df['NAME'].values
    # these will become Passenger()'s

    # Initialize airports
    airports = initialize_airports(airport_names)

    # Initialize flights
    initialize_flights(flight_info, airports)

    # Display the airport data created thus far
    print_data(airports)

    for airport in airports:
        for flight in airport.get_flights():
            for i in range(25 + np.random.randint(0, 200)):
                passenger = Passenger(names[np.random.choice(len(names), 1)])
                flight.add_passenger(passenger)


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


def initialize_flights(flight_info, airports):
    # Go through the airports and pass in flight information
    for i in range(len(airports)):
        # Create a new flight for this airport
        airports[i].add_flight(Flight())

        # Get all flights for this airport
        flights = airports[i].get_flights()
        # Go through the flights and set all fields
        for flight in flights:
            flight.set_current_airport(airports[i])
            flight.set_destination_airport(
                airports[i+1] if i < len(airports)-1 else airports[0])
            flight.set_flight_number(flight_info[i][0])
            flight.set_airline(flight_info[i][1])
            flight.set_flight_date(flight_info[i][2])
            flight.set_flight_time(flight_info[i][3])

def print_data(airports):
    for airport in airports:
        for flight in airport.get_flights():
            print(flight)


main()
