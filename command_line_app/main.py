import sys

clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Software engineer'
    },
    {
        'name': 'Raul',
        'company': 'Facebook',
        'email': 'raul@facebook.com',
        'position': 'Data engineer'
    },
]


def create_client(client):
    if client not in clients:
        clients.append(client)
        list_clients()
    else:
        print('The client already exists in the list')


def update_client(client_id, update_client):
    if len(clients) - 1 >= client_id:
        clients[client_id] = update_client
        list_clients()
    else:
        _client_not_exist()


def delete_client(client_id):
    if len(clients) - 1 >= client_id:
        clients.pop(client_id)
        list_clients()
    else:
        _client_not_exist()


def search_client(client_name):   
    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True


def list_clients():
    print('uid |  name  | company  | email  | position ')
    print('*' *50)

    for idx, client in enumerate(clients):
        print(f'{idx} | {client["name"]} | {client["company"]} | {client["email"]} | {client["position"]}')


def _print_welcome():
    print('WELCOME TO THIS APP MADE WITH PYTHON')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')


def _get_data_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }

    return client


def _client_not_exist():
    print('The client does not exist')


def _get_client_field(field_name):
    field = None

    while not field:
        field = input(f'What is the client {field_name}? ')

        if field_name == 'exit':
            field = None
            break

    if not field:
        sys.exit()

    return field;


if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client = _get_data_from_user()
        create_client(client)
    elif command == 'U':
        client_id = int(_get_client_field('id'))
        client_data = _get_data_from_user()
        update_client(client_id, client_data)
    elif command == 'D':
        client_id = int(_get_client_field('id'))
        delete_client(client_id)
    elif command == 'S':
        client_name = _get_client_field('name')
        found = search_client(client_name)
        
        if found:
            print('The client is on the list')
        else:
            print(f'Client {client_name} is not on the list')
    else:
        print('Invalid command')