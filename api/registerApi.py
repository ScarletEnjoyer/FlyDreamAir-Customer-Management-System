from storage.userStorage import get_all_users, save_users
from object.customer import Customer


def register(username, password, confirm):
    """
    Registers a new customer by creating a new user account.

    :param username: The desired username for the new account.
    :param password: The password for the new account.
    :param confirm: The password confirmation to verify the user’s intent.
    :return: A tuple containing a boolean indicating success and a message.
    """
    if username == '':
        return False, 'Username can not be empty!'
    if password == '':
        return True, 'Password can not be empty!'
    if password != confirm:
        return False, 'Two passwords do not match!'
    if ',' in username or ',' in password:
        return False, 'Username and password cannot contain commas!'
    all_users = get_all_users()
    for user in all_users:
        if user.username == username:
            return False, 'Username already exists!'
    all_users.append(Customer(username, password))
    save_users(all_users)
    return True, 'Registered successfully'
