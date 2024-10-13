class Countries:
    """
    A class to manage a collection of countries.

    Attributes
    ----------
    countries : dict
        A dictionary that maps country names to their respective Country objects.

    Methods
    -------
    add_country(country)
        Adds a Country object to the collection.

    get_countries_names()
        Returns a sorted list of country names in the collection.

    get_country_by_name(country_name)
        Retrieves a Country object by its name, if it exists in the collection.
    """
    def __init__(self):
        """
        Initializes the Countries object with an empty dictionary for storing Country objects.
        """
        self.countries = {}

    def add_country(self, country):
        """
        Adds a Country object to the collection, using the country name as the key.

        :param country: An instance of the Country class to be added.
        """
        self.countries[country.country_name] = country

    def get_countries_names(self):
        """
        Returns a sorted list of the names of all countries in the collection.

        :return: A sorted list of country names.
        """
        names = sorted(self.countries.keys())
        return names

    def get_country_by_name(self, country_name):
        """
        Retrieves a Country object by its name from the collection.

        :param country_name: The name of the country to retrieve.
        :return: The corresponding Country object, or None if the country is not found.
        """
        if country_name in self.countries:
            return self.countries[country_name]
        return None
