from object.reservation import Reservation
from storage.reservationStorage import *
from storage.flightStorage import *


def book_flight(username, flight, selected_seat_class, selected_seat, services):
    """
    Books a flight for a user by creating a reservation.

    :param username: The username of the customer making the reservation.
    :param flight: The flight object that the user wants to book.
    :param selected_seat_class: The class of the seat (e.g., Economy, Business, First).
    :param selected_seat: The specific seat number selected by the user.
    :param services: A list of additional services selected by the user for the reservation.
    """
    reservation = Reservation(username, flight, selected_seat_class, selected_seat, services)
    reservations = get_all_reservations()
    reservations.append(reservation)
    save_reservations(reservations)


def cancel_reservation(reservation):
    """
    Cancels a reservation for a flight.

    :param reservation: The Reservation object that needs to be canceled.
    """
    reservations = get_all_reservations()
    reservation_to_remove = None
    for reservation_2 in reservations:
        if reservation_2.username == reservation.username and reservation_2.flight.flight_number == reservation.flight.flight_number and reservation_2.selected_seat_class == reservation.selected_seat_class and reservation_2.selected_seat == reservation.selected_seat:
            reservation_to_remove = reservation_2
            break
    if reservation_to_remove is not None:
        reservations.remove(reservation_to_remove)
    save_reservations(reservations)
    flights = get_all_flights()
    for flight in flights:
        if flight.flight_number == reservation.flight.flight_number:
            flight.seats[reservation.selected_seat_class]['available_seats'].append(reservation.selected_seat)
    save_flights(flights)


def clear_reservations():
    save_reservations([])
