clients = 'Pablo,Ricardo,'

def create_client(client_name):
    global clients

    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print('The client already exists in the list')


def list_clients():
    global clients
    print(clients)


def _add_comma():
    global clients
    clients += ','


def _print_welcome():
    print('WELCOME TO THIS APP MADE WITH PYTHON')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[D]elete client')


if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.lower()

    if command == 'c':
        client_name = input('What is the client name? ')
        create_client(client_name)
        list_clients()
    elif command == 'd':
        pass
    else:
        print('Invalid command')