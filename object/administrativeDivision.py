class AdministrativeDivision:
    """
    A class to represent an administrative division (e.g., state, county, city).

    Attributes
    ----------
    name : str
        The name of the administrative division.
    next_level_divisions : dict
        A dictionary mapping the names of the next-level divisions to their respective
        AdministrativeDivision objects.

    Methods
    -------
    add_next_level_division(division)
        Adds a lower-level division under the current division.

    get_next_level_divisions_names()
        Returns a sorted list of names of the next-level divisions.
    """
    def __init__(self, name):
        """
        Initializes the AdministrativeDivision with a name and an empty dictionary for storing next-level divisions.

        :param name: The name of the administrative division.
        """
        self.name = name
        self.next_level_divisions = {}

    def add_next_level_division(self, division: 'AdministrativeDivision'):
        """
        Adds a next-level administrative division to the current division.

        :param division: An instance of AdministrativeDivision representing the next-level division.
        """
        self.next_level_divisions[division.name] = division

    def get_next_level_divisions_names(self):
        """
        Returns the names of all next-level administrative divisions sorted alphabetically.

        :return: A sorted list of next-level division names.
        """
        return sorted(self.next_level_divisions.keys())