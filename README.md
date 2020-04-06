# CS205-Pair-Project-BCJV

## Ben Caruso
## Jamie Voynow

For our object-oriented model of data, we chose to model an airport as well as flights that depart and arrive at the airport. Airports and flights have a many to two relationship, as each airport can have many flights while each flight has exactly two airports - the airport it departs from and the airport it arrives at. Flights and passengers have a many to one relationship, since flights obviously can have many passengers while each passenger is assigned one flight. These relationships were taken into account during the design of our classes. 

## Class Breakdown by Entity

### Airport: 

name: string

flights: list of Flights

max_flights: int

### Flight:

flight_number: string

airline: string

passengers: list of Passengers

current_airport: Airport

destination_airport: Airport

flight_date: string

flight_time: string

### Passenger:

name: string

flight: Flight

Our unit tests reflect common use scenarios we anticipate for our model. Such scenarios include adding a passenger to a flight, connecting flights with corresponding airports, and dealing with the cancellation of a flight.

