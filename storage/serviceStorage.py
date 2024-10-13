import os
import pickle
from object.service import Service

SERVICE_STORAGE_FILE = 'services.pkl'


def get_all_services():
    """
    Retrieves all services from the storage file.

    Checks if the storage file exists. If it does, it loads and returns
    the list of services. If the file does not exist, it returns an empty list.

    :return: A list of Service objects stored in the file, or an empty list if no services are stored.
    """
    if not os.path.exists(SERVICE_STORAGE_FILE):
        return []
    with open(SERVICE_STORAGE_FILE, 'rb') as f:
        services = pickle.load(f)
    return services


def save_services(services: list[Service]):
    """
    Saves the list of services to the storage file.

    This function takes a list of Service objects and writes it to the
    specified storage file using the pickle module.

    :param services: A list of Service objects to be saved.
    """
    with open(SERVICE_STORAGE_FILE, 'wb') as f:
        pickle.dump(services, f)
