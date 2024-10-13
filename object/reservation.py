class Reservation:
    """
    A class to represent a flight reservation made by a user.

    Attributes
    ----------
    username : str
        The username of the individual making the reservation.
    flight : Flight
        An instance of the Flight class representing the flight being reserved.
    selected_seat_class : str
        The class of the seat selected for the reservation (e.g., 'Economy class', 'Business class', 'First class').
    selected_seat : int
        The seat number that has been selected for the reservation.
    services : list
        A list of Service objects representing additional services selected with the reservation.

    Methods
    -------
    (none currently)
    """

    def __init__(self, username, flight, selected_seat_class, selected_seat, services):
        """
        Initializes a Reservation object with the specified details.

        :param username: The username of the individual making the reservation.
        :param flight: An instance of the Flight class representing the flight being reserved.
        :param selected_seat_class: The class of the seat selected for the reservation.
        :param selected_seat: The seat number that has been selected for the reservation.
        :param services: A list of Service objects representing additional services selected with the reservation.
        """
        self.username = username
        self.flight = flight
        self.selected_seat_class = selected_seat_class
        self.selected_seat = selected_seat
        self.services = services
