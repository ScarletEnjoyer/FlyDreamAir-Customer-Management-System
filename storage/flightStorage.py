import os
import pickle

from object.flight import Flight

FLIGHT_STORAGE_FILE = 'flights.pkl'


def get_all_flights():
    """
    Retrieves all flights from the storage file.

    Checks if the storage file exists. If it does, it loads and returns
    the list of flights. If the file does not exist, it returns an empty list.

    :return: A list of Flight objects stored in the file, or an empty list if no flights are stored.
    """
    if not os.path.exists(FLIGHT_STORAGE_FILE):
        return []
    with open(FLIGHT_STORAGE_FILE, 'rb') as f:
        flights = pickle.load(f)
    return flights


def save_flights(flights: list[Flight]):
    """
    Saves the list of flights to the storage file.

    This function takes a list of Flight objects and writes it to the
    specified storage file using the pickle module.

    :param flights: A list of Flight objects to be saved.
    """
    with open(FLIGHT_STORAGE_FILE, 'wb') as f:
        pickle.dump(flights, f)
