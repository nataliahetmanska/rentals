import keyring


def save_credentials(service_name='wheelie'):
    keyring.set_password(service_name, username=username, password=password)

if __name__ == '__main__':
    username = str(input("Enter username: "))
    password = str(input("Enter password: "))
    save_credentials(username, password)
