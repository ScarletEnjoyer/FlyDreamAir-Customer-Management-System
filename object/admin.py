from object.user import User


class Admin(User):
    """
    A class to represent an admin user, inheriting from the User class.

    Inherits all attributes from the User class.

    Methods
    -------
    __init__(username, password)
        Initializes the Admin object with a username and password, using the parent class User.

    __str__()
        Returns a string representation of the Admin object.
    """
    def __init__(self, username, password):
        """
        Initializes the Admin object by calling the constructor of the parent User class.

        :param username: The admin's username.
        :param password: The admin's password.
        """
        super().__init__(username, password)

    def __str__(self):
        """
        Returns a string representation of the Admin object.

        :return: A string in the format 'Admin,username,password'.
        """
        return f'Admin,{self.username},{self.password}'
