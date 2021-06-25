import sys
import os
import csv

CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []


def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, 'r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)


def _save_clients_to_storage():
    tmp_table_name = f'{CLIENT_TABLE}.tmp'
    with open(tmp_table_name, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

        os.remove(CLIENT_TABLE)
        os.rename(tmp_table_name, CLIENT_TABLE)


def create_client(client):
    if client not in clients:
        clients.append(client)
    else:
        print('The client already exists in the list')


def update_client(client_id, update_client):
    if len(clients) - 1 >= client_id:
        clients[client_id] = update_client
    else:
        _client_not_exist()


def delete_client(client_id):
    if len(clients) - 1 >= client_id:
        clients.pop(client_id)
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
    print('[L]ist clients')


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

        if field == 'exit':
            field = None
            break

    if not field:
        sys.exit()

    return field;


if __name__ == '__main__':
    _initialize_clients_from_storage()
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
    elif command == 'L':
        list_clients()
    elif command == 'S':
        client_name = _get_client_field('name')
        found = search_client(client_name)
        
        if found:
            print('The client is on the list')
        else:
            print(f'Client {client_name} is not on the list')
    else:
        print('Invalid command')

    _save_clients_to_storage()