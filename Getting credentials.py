import keyring


def save_credentials(service_name='wheelie'):
    username = str(input("Enter username: "))
    password = str(input("Enter password: "))

    keyring.set_password(service_name, username=username, password=password)

