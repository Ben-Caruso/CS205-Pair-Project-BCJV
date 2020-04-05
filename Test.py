import unittest
from passenger import Passenger
from flight import Flight
from airport import Airport


class TestModel(unittest.TestCase):
    airport = None

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
        cls.flightJFKToLogan = Flight.airports_to_from(cls.JFK, cls.Logan)
        # Flight 1
        cls.flightLoganToJFK.set_flight_number("UA1161")
        cls.flightLoganToJFK.set_flight_date("04-27-2020")
        cls.flightLoganToJFK.set_flight_time("4:30pm")
        cls.flightLoganToJFK.set_airline("United Airlines")
        # Flight 2
        cls.flightJFKToLogan.set_flight_number("SP9374")
        cls.flightJFKToLogan.set_flight_date("04-28-2020")
        cls.flightJFKToLogan.set_flight_time("6:30am")
        cls.flightJFKToLogan.set_airline("Spirit Airlines")

        # Add passengers to flight
        cls.flightJFKToLogan.add_passenger(cls.Julia)
        cls.flightJFKToLogan.add_passenger(cls.Jamie)

        # Add flights to airport
        cls.Logan.add_flight(cls.flightLoganToJFK)
        cls.Logan.add_flight(cls.flightLoganToJFK)
        cls.JFK.add_flight(cls.flightJFKToLogan)
        cls.JFK.add_flight(cls.flightJFKToLogan)

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

    def test_flight_one(self):
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

if __name__ == '__main__':
    unittest.main()
