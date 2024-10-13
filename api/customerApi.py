from storage.userStorage import get_all_users, save_users


def change_password(customer_name, new_password):
    users = get_all_users()
    for user in users:
        if user.username == customer_name:
            user.password = new_password
    save_users(users)


def clear_customers():
    users = get_all_users()
    users = [user for user in users if user.username == 'admin']
    save_users(users)