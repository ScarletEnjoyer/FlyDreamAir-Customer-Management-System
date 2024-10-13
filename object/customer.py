from object.user import User


class Customer(User):
    """
    A class to represent a customer user, inheriting from the User class.

    Inherits all attributes from the User class.

    Methods
    -------
    __init__(username, password)
        Initializes the Customer object with a username and password, using the parent class User.

    __str__()
        Returns a string representation of the Customer object.
    """
    def __init__(self, username, password):
        """
        Initializes the Customer object by calling the constructor of the parent User class.

        :param username: The customer's username.
        :param password: The customer's password.
        """
        super().__init__(username, password)

    def __str__(self):
        """
        Returns a string representation of the Customer object.

        :return: A string in the format 'Customer,username,password'.
        """
        return f'Customer,{self.username},{self.password}'
