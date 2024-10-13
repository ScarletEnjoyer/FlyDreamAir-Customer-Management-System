from object.administrativeDivision import AdministrativeDivision


class Country:
    """
    A class to represent a country, which contains multiple administrative divisions (e.g., states, provinces).

    Attributes
    ----------
    country_code : str
        The code representing the country (e.g., "US" for the United States).
    country_name : str
        The full name of the country.
    administrative_divisions : dict
        A dictionary mapping the names of the first-level administrative divisions (admin1)
        to their respective AdministrativeDivision objects.

    Methods
    -------
    add_administrative_division(division)
        Adds a first-level administrative division (admin1) to the country.

    get_admin1_names()
        Returns a sorted list of names of the first-level administrative divisions.

    get_admin1_by_name(admin1_name)
        Retrieves an AdministrativeDivision object by its name.
    """
    def __init__(self, country_code, country_name):
        """
        Initializes the Country object with a country code, country name, and an empty dictionary
        for storing first-level administrative divisions.

        :param country_code: The code representing the country.
        :param country_name: The full name of the country.
        """
        self.country_code = country_code
        self.country_name = country_name
        self.administrative_divisions = {}

    def add_administrative_division(self, division: AdministrativeDivision):
        """
        Adds a first-level administrative division (admin1) to the country's administrative divisions.

        :param division: An instance of AdministrativeDivision representing the next-level division (admin1).
        """
        self.administrative_divisions[division.name] = division

    def get_admin1_names(self):
        """
        Returns a sorted list of names of the first-level administrative divisions.

        :return: A sorted list of admin1 division names.
        """
        names = sorted(self.administrative_divisions.keys())
        return names

    def get_admin1_by_name(self, admin1_name):
        """
        Retrieves an AdministrativeDivision object by its name from the first-level administrative divisions.

        :param admin1_name: The name of the first-level administrative division (admin1).
        :return: The corresponding AdministrativeDivision object.
        """
        return self.administrative_divisions[admin1_name]
