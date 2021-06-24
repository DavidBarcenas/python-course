clients = 'Pablo,Ricardo,'

def create_client(client_name):
    global clients

    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print('The client already exists in the list')


def update_client(client_name, update_client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', update_client_name + ',')
    else:
        _client_not_exist()


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', '')
    else:
        _client_not_exist()


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
    print('[U]pdate client')
    print('[D]elete client')


def _client_not_exist():
    print('The client does not exist')


def _get_client_name():
    return input('What is the client name? ')


if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        update_client_name = input('What is the updated client name? ')
        update_client(client_name,update_client_name)
        list_clients()
    else:
        print('Invalid command')