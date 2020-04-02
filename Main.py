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
    # pick 400 names with replacement
    names = names[np.random.choice(len(names), 400)]
    # these will become Passenger()'s

    airports = initialize_airports(airport_names)
    for i in range(len(airports)):
        airports[i].add_flight(Flight())

        flights = airports[i].get_flights()
        for flight in flights:
            flight.set_current_airport(airports[i])
            flight.set_destination_airport(
                airports[i+1] if i < len(airports)-1 else airports[0])
            flight.set_flight_number(flight_info[i][0])
            flight.set_airline(flight_info[i][1])
            flight.set_flight_date(flight_info[i][2])
            flight.set_flight_time(flight_info[i][3])

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
