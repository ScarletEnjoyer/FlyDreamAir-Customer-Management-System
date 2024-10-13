from storage.serviceStorage import get_all_services, save_services
from object.service import Service


def get_services():
    """
    Retrieves all available services.

    :return: A list of Service objects representing all the services.
    """
    return get_all_services()


def add_service(name, unit_price):
    """
    Adds a new service if it does not already exist.

    :param name: The name of the service to be added.
    :param unit_price: The unit price of the service. Must be non-negative.
    :return: A tuple containing a boolean indicating success or failure,
             and a message providing additional information.
    """
    services = get_all_services()
    for service in services:
        if service.name == name:
            return False, 'Service already exists!'
    if unit_price < 0:
        return False, 'Unit price cannot be negative!'
    services.append(Service(name, unit_price))
    save_services(services)
    return True, 'Added successfully!'
