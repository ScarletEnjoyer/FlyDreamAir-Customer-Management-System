import re

from storage.flightStorage import get_all_flights, save_flights
from object.flight import Flight


def validate_flight_number(flight_number):
    """
    Validates the flight number format.

    :param flight_number: The flight number to validate.
    :return: True if the flight number is valid, otherwise False.
    """
    return bool(re.match(r'^[A-Z]{2}\d{3}$', flight_number))


def flight_number_exists(flight_number):
    """
    Checks if a flight number already exists in the stored flights.

    :param flight_number: The flight number to check.
    :return: True if the flight number exists, otherwise False.
    """
    flights = get_all_flights()
    for flight in flights:
        if flight.flight_number == flight_number:
            return True
    return False


def validata_location(country_from, admin1_from, admin2_from, country_to, admin1_to, admin2_to):
    """
    Validates the origin and destination locations of the flight.

    :param country_from: The country of origin.
    :param admin1_from: The first-level administrative division of origin.
    :param admin2_from: The second-level administrative division of origin.
    :param country_to: The destination country.
    :param admin1_to: The first-level administrative division of the destination.
    :param admin2_to: The second-level administrative division of the destination.
    :return: True if the locations are valid (i.e., not the same), otherwise False.
    """
    if country_from == country_to and admin1_from == admin1_to and admin2_from == admin2_to:
        return False
    return True


def validate_time(departure_time, arrival_time):
    """
    Validates that the departure time is before the arrival time.

    :param departure_time: The scheduled departure time.
    :param arrival_time: The scheduled arrival time.
    :return: True if the departure time is before the arrival time, otherwise False.
    """
    return departure_time < arrival_time


def validate_class(economy_class_count, business_class_count, first_class_count):
    """
    Validates that at least one class has available seats.

    :param economy_class_count: The number of economy class seats.
    :param business_class_count: The number of business class seats.
    :param first_class_count: The number of first class seats.
    :return: True if at least one class has seats, otherwise False.
    """
    return economy_class_count != 0 or business_class_count != 0 or first_class_count != 0


def add_flight(flight_number, country_from, admin1_from, admin2_from, country_to, admin1_to, admin2_to, departure_time, arrival_time, economy_class_count, business_class_count, first_class_count, economy_class_price, business_class_price,
               first_class_price):
    """
    Adds a new flight to the system after validating its details.

    :param flight_number: The flight number.
    :param country_from: The country of origin.
    :param admin1_from: The first-level administrative division of origin.
    :param admin2_from: The second-level administrative division of origin.
    :param country_to: The destination country.
    :param admin1_to: The first-level administrative division of the destination.
    :param admin2_to: The second-level administrative division of the destination.
    :param departure_time: The scheduled departure time.
    :param arrival_time: The scheduled arrival time.
    :param economy_class_count: The number of economy class seats.
    :param business_class_count: The number of business class seats.
    :param first_class_count: The number of first class seats.
    :param economy_class_price: The price per economy class seat.
    :param business_class_price: The price per business class seat.
    :param first_class_price: The price per first class seat.
    :return: A tuple (success: bool, message: str).
    """
    if not validate_flight_number(flight_number):
        return False, 'Invalid flight number.'
    if not validata_location(country_from, admin1_from, admin2_from, country_to, admin1_to, admin2_to):
        return False, 'Invalid from...to.'
    if not validate_time(departure_time, arrival_time):
        return False, 'Invalid departure time and arrival time.'
    if not validate_class(economy_class_count, business_class_count, first_class_count):
        return False, 'Invalid departure time and arrival time.'
    if flight_number_exists(flight_number):
        return False, 'flight number already exists.'
    if economy_class_count > 0 >= economy_class_price:
        return False, 'Unit price for economy class must be greater than 0'
    if business_class_count > 0 >= business_class_price:
        return False, 'Unit price for business class must be greater than 0'
    if first_class_count > 0 >= first_class_price:
        return False, 'Unit price for first class must be greater than 0'
    flights = get_all_flights()
    flights.append(Flight(flight_number, country_from, admin1_from, admin2_from, country_to, admin1_to, admin2_to, departure_time, arrival_time, economy_class_count, business_class_count, first_class_count, economy_class_price, business_class_price,
                          first_class_price))
    save_flights(flights)
    return True, 'Add flight successfully.'


def get_flights():
    """
    Retrieves all flights from storage.

    :return: A list of all Flight objects.
    """
    return get_all_flights()


def remove_flight(flight):
    """
    Removes a flight from the system.

    :param flight: The Flight object to remove.
    """
    flights = get_flights()
    to_remove_flight = None
    for i in range(len(flights)):
        if flights[i].flight_number == flight.flight_number:
            to_remove_flight = flights[i]
            break
    flights.remove(to_remove_flight)
    save_flights(flights)


def get_available_seats(flight):
    """
    Retrieves available seats for a specific flight.

    :param flight: The Flight object for which to get available seats.
    :return: A dictionary of available seats categorized by class.
    """
    seat_classes = {}
    for seat_class in flight.seats.keys():
        if len(flight.seats[seat_class]['available_seats']) != 0:
            seat_classes[seat_class] = {
                'unit_price': flight.seats[seat_class]['unit_price'],
                'available_seats': flight.seats[seat_class]['available_seats']
            }
    return seat_classes


def remove_seat(flight_number, seat_class, seat):
    """
    Removes a specific seat from the available seats of a flight.

    :param flight_number: The flight number from which to remove the seat.
    :param seat_class: The class of the seat (e.g., Economy, Business, First).
    :param seat: The seat number to remove.
    """
    flights = get_flights()
    for flight in flights:
        if flight.flight_number == flight_number:
            flight.seats[seat_class]['available_seats'].remove(seat)
            break
    save_flights(flights)


def clear_flights():
    save_flights([])
