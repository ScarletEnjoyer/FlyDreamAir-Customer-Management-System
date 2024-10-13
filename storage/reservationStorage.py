import os
import pickle

from object.reservation import Reservation

RESERVATION_STORAGE_FILE = 'reservations.pkl'


def get_all_reservations():
    """
    Retrieves all reservations from the storage file.

    Checks if the storage file exists. If it does, it loads and returns
    the list of reservations. If the file does not exist, it returns an empty list.

    :return: A list of Reservation objects stored in the file, or an empty list if no reservations are stored.
    """
    if not os.path.exists(RESERVATION_STORAGE_FILE):
        return []
    with open(RESERVATION_STORAGE_FILE, 'rb') as f:
        reservations = pickle.load(f)
    return reservations


def get_reservations_by_username(username):
    """
    Retrieves all reservations associated with a specific username.

    This function calls `get_all_reservations` to obtain the complete list of reservations
    and filters them based on the provided username.

    :param username: The username for which to retrieve reservations.
    :return: A list of Reservation objects associated with the given username.
    """
    reservations = []
    for reservation in get_all_reservations():
        if reservation.username == username:
            reservations.append(reservation)
    return reservations


def save_reservations(reservations):
    """
    Saves the list of reservations to the storage file.

    This function takes a list of Reservation objects and writes it to the
    specified storage file using the pickle module.

    :param reservations: A list of Reservation objects to be saved.
    """
    with open(RESERVATION_STORAGE_FILE, 'wb') as f:
        pickle.dump(reservations, f)
