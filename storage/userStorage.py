import os
from object.user import User
from object.admin import Admin
from object.customer import Customer

USER_STORAGE_FILE = 'users.txt'


def init_user_storage():
    """
    Initializes the user storage file if it does not already exist.

    If the user storage file is not found, it creates a default Admin user
    and saves it to the file.
    """
    if not os.path.exists(USER_STORAGE_FILE):
        users = [Admin('admin', 'admin')]
        save_users(users)


def get_all_users():
    """
    Retrieves all users from the storage file.

    Reads the user storage file, parses each line, and creates instances of
    Admin or Customer based on the stored data.

    :return: A list of User objects (Admin and Customer) retrieved from the file.
    """
    with open(USER_STORAGE_FILE, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    users = []
    for line in lines:
        tokens = line.split(',')
        if len(tokens) == 3:
            if tokens[0] == 'Admin':
                users.append(Admin(tokens[1], tokens[2]))
            elif tokens[0] == 'Customer':
                users.append(Customer(tokens[1], tokens[2]))
    return users


def save_users(users: list[User]):
    """
    Saves the list of users to the storage file.

    This function takes a list of User objects (Admin and Customer)
    and writes their string representations to the specified storage file.

    :param users: A list of User objects to be saved.
    """
    with open(USER_STORAGE_FILE, 'w') as f:
        for user in users:
            f.write(str(user))
            f.write('\n')




