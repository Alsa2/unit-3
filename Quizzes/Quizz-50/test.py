import pytest
from script import Flights

def test_get_duration():
    # Create an instance of class Flights
    flight = Flights('QF456', 'SFO', 'SYD', '6:00pm', [7, 25, 5])
    
    # Assert the output of get_duration()
    assert flight.get_duration() == "7 hours 25 minutes and 5 seconds"
