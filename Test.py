import unittest
from passenger import Passenger
from flight import Flight
from airport import Airport


class TestModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass()")

        # Initialize airports
        cls.Logan = Airport()
        cls.JFK = Airport()
        cls.Logan.set_name("Logan")
        cls.JFK.set_name("JFK")

        # Initialize passengers
        cls.Ben = Passenger("Ben")
        cls.Julia = Passenger("Julia")
        cls.Jamie = Passenger("Jamie")

        # Initialize flights
        cls.flightLoganToJFK = Flight.airports_to_from(cls.Logan, cls.JFK)
        # Flight 1
        cls.flightLoganToJFK.set_flight_number("UA1161")
        cls.flightLoganToJFK.set_flight_date("04-27-2020")
        cls.flightLoganToJFK.set_flight_time("4:30pm")
        cls.flightLoganToJFK.set_airline("United Airlines")

        # Add flights to airport
        cls.Logan.add_flight(cls.flightLoganToJFK)
        cls.JFK.add_flight(cls.flightLoganToJFK)

    @classmethod
    def tearDownClass(cls):
        # Tears down entire class at the end
        print("tearDownClass()")

    def setUp(self) -> None:
        # Sets up before each testing suite
        print("setUp()")

    def tearDown(self) -> None:
        # Tears down each testing suite after test
        print("tearDown()")

# -------------- Testing Functions ----------- #

    # Test passenger getting ticket for existing flight
    def test_passenger(self):
        # Check that flight1 does not have Ben registered as a passenger
        passengers_flight1 = self.flightLoganToJFK.get_passengers()
        self.assertEqual(len(passengers_flight1), 0)

        # Now Ben bought a ticket to flight1
        # Check that he is now a passenger
        # Get_passengers on this flight should return a list containing only Ben
        self.flightLoganToJFK.add_passenger(self.Ben)
        self.assertEqual([self.Ben], self.flightLoganToJFK.get_passengers())

        # Now check that Ben has the given flight going from Logan to JFK
        self.assertEqual(self.Ben.get_flight(), self.flightLoganToJFK)

    # Test creation of a new flight from a new airport
    def test_flight_creation(self):
        # Create a new airport - LAX
        self.LAX = Airport()
        self.LAX.set_name("LAX")

        # Check that the LAX airport currently has no flights
        LAXflights = self.LAX.get_flights()
        self.assertEqual(len(LAXflights), 0)

        # Create a new flight from LAX to Logan
        self.flightLAXToLogan = Flight.airports_to_from(self.LAX, self.Logan)
        self.flightLAXToLogan.set_flight_number("UA2274")
        self.flightLAXToLogan.set_flight_date("04-26-2020")
        self.flightLAXToLogan.set_flight_time("9:30pm")
        self.flightLAXToLogan.set_airline("United Airlines")

        # Add the new flight to LAX and Logan's flights
        self.Logan.add_flight(self.flightLAXToLogan)
        self.LAX.add_flight(self.flightLAXToLogan)

        # Check that the LAX airport now has this flight outgoing
        LAXflights = self.LAX.get_outgoing_flights()
        self.assertEqual(len(LAXflights), 1)
        self.assertEqual(LAXflights, [self.flightLAXToLogan])

        # Check that Logan airport now has this flight incoming
        Loganflights = self.Logan.get_incoming_flights()
        self.assertEqual(Loganflights, [self.flightLAXToLogan])

        # Remove flight in order to clean up for next test case
        self.Logan.remove_flight(self.flightLAXToLogan)
        self.LAX.remove_flight(self.flightLAXToLogan)

    # Test the case that flightJFKtoLogan gets cancelled
    def test_flight_cancel(self):
        # Create new flight from JFK to Logan
        self.flightJFKToLogan = Flight.airports_to_from(self.JFK, self.Logan)
        self.flightJFKToLogan.set_flight_number("SP9374")
        self.flightJFKToLogan.set_flight_date("04-28-2020")
        self.flightJFKToLogan.set_flight_time("6:30am")
        self.flightJFKToLogan.set_airline("Spirit Airlines")
        # Add flight to Logan and JFK
        self.Logan.add_flight(self.flightJFKToLogan)
        self.JFK.add_flight(self.flightJFKToLogan)

        # Double check that Logan has this flight
        self.assertEqual([self.flightJFKToLogan], self.Logan.get_incoming_flights())

        # Add a new passenger to flight
        self.flightJFKToLogan.add_passenger(self.Jamie)

        # Double check that the passenger has this flight and vice versa
        self.assertEqual([self.Jamie], self.flightJFKToLogan.get_passengers())
        self.assertEqual(self.Jamie.get_flight(), self.flightJFKToLogan)

        # Now, the flight got cancelled. Remove from airport
        self.Logan.remove_flight(self.flightJFKToLogan)
        self.JFK.remove_flight(self.flightJFKToLogan)

        # Check that the airport does not have this flight
        LoganIncoming = self.Logan.get_incoming_flights()
        self.assertEqual(len(LoganIncoming), 0)

        # Check that the passenger no longer has this flight as it is cancelled
        self.assertEqual(self.Jamie.get_flight(), None)



if __name__ == '__main__':
    unittest.main()
