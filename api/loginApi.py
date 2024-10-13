from storage.userStorage import get_all_users
from object.admin import Admin
from object.customer import Customer


def get_user(username, password, user_type):
    """
    Retrieves a user based on the provided username, password, and user type.

    :param username: The username of the user.
    :param password: The password of the user.
    :param user_type: The type of the user (either 'Admin' or 'Customer').
    :return: The user object if found and matches the criteria, otherwise None.
    """
    users = get_all_users()
    for user in users:
        if username == user.username and password == user.password:
            if user_type == 'Admin' and isinstance(user, Admin):
                return user
            elif user_type == 'Customer' and isinstance(user, Customer):
                return user
    return None


def login(username, password, user_type):
    """
    Authenticates a user based on username, password, and user type.

    :param username: The username of the user.
    :param password: The password of the user.
    :param user_type: The type of the user (either 'Admin' or 'Customer').
    :return: A tuple containing the user object (if authenticated) and a message.
    """
    if username == '':
        return None, 'Username can not be empty!'
    if password == '':
        return None, 'Password can not be empty!'
    user = get_user(username, password, user_type)
    if user is None:
        return None, 'username or password is incorrect!'
    return user, ''


def is_admin(user):
    """
    Checks if the provided user is an admin.

    :param user: The user object to check.
    :return: True if the user is an Admin, otherwise False.
    """
    return isinstance(user, Admin)
