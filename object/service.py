class Service:
    """
    A class to represent a service offered, including its name and price.

    Attributes
    ----------
    name : str
        The name of the service.
    unit_price : float
        The price of a single unit of the service.

    Methods
    -------
    (none currently)
    """
    def __init__(self, name, unit_price):
        """
        Initializes a Service object with the specified name and unit price.

        :param name: The name of the service.
        :param unit_price: The price of a single unit of the service.
        """
        self.name = name
        self.unit_price = unit_price
