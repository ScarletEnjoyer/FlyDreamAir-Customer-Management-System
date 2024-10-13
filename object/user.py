class User:
    """
    A class to represent a user in the system.

    Attributes
    ----------
    username : str
        The username associated with the user account.
    password : str
        The password for the user account.
    """
    def __init__(self, username, password):
        """
        Initializes a new User object with a username and a password.
        :param username: The user's chosen username.
        :param password: The user's chosen password.
        """
        self.username = username
        self.password = password
