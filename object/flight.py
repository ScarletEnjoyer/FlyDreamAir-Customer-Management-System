class Flight:
    """
    A class to represent a flight and its associated details, including seat availability and pricing.

    Attributes
    ----------
    flight_number : str
        The unique identifier for the flight.
    country_from : str
        The country from which the flight departs.
    admin1_from : str
        The first-level administrative division (e.g., state or province) of the departure location.
    admin2_from : str
        The second-level administrative division (e.g., city or county) of the departure location.
    country_to : str
        The country to which the flight is heading.
    admin1_to : str
        The first-level administrative division of the destination.
    admin2_to : str
        The second-level administrative division of the destination.
    departure_time : str
        The scheduled departure time of the flight.
    arrival_time : str
        The scheduled arrival time of the flight.
    seats : dict
        A dictionary storing information about seat classes, their availability, and pricing.
        Contains three classes: 'Economy class', 'Business class', and 'First class'.
        Each class has the following keys:
            - 'count': The total number of seats in the class.
            - 'available_seats': A list of available seat numbers.
            - 'unit_price': The price per seat in the class.

    Methods
    -------
    (none currently)
    """
    def __init__(self, flight_number, country_from, admin1_from, admin2_from, country_to, admin1_to, admin2_to, departure_time, arrival_time, economy_class_count, business_class_count, first_class_count, economy_class_price, business_class_price,
                 first_class_price):
        """
        Initializes a Flight object with the provided flight details, seat counts, and pricing.

        :param flight_number: The unique identifier for the flight.
        :param country_from: The country from which the flight departs.
        :param admin1_from: The first-level administrative division of the departure location.
        :param admin2_from: The second-level administrative division of the departure location.
        :param country_to: The country to which the flight is heading.
        :param admin1_to: The first-level administrative division of the destination.
        :param admin2_to: The second-level administrative division of the destination.
        :param departure_time: The scheduled departure time of the flight.
        :param arrival_time: The scheduled arrival time of the flight.
        :param economy_class_count: The total number of economy class seats.
        :param business_class_count: The total number of business class seats.
        :param first_class_count: The total number of first class seats.
        :param economy_class_price: The price for an economy class seat.
        :param business_class_price: The price for a business class seat.
        :param first_class_price: The price for a first class seat.
        """
        self.flight_number = flight_number

        self.country_from = country_from
        self.admin1_from = admin1_from
        self.admin2_from = admin2_from
        self.country_to = country_to
        self.admin1_to = admin1_to
        self.admin2_to = admin2_to

        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.seats = {
            'Economy class': {
                'count': economy_class_count,
                'available_seats': [(i + 1) for i in range(economy_class_count)],
                'unit_price': economy_class_price
            },
            'Business class': {
                'count': business_class_count,
                'available_seats': [(i + 1) for i in range(business_class_count)],
                'unit_price': business_class_price
            },
            'First class': {
                'count': first_class_count,
                'available_seats': [(i + 1) for i in range(first_class_count)],
                'unit_price': first_class_price
            }
        }
