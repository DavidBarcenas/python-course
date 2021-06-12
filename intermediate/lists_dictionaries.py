def list_comprehensions():
    # squares = []
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         squares.append(i**2)

    squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    print(squares)

    challenge = [i for i in range(1, 999) if i%4 == 0 and i%6 == 0 and i%9 == 0]
    print(challenge)

def list_and_dicts():
    my_list = [1, 'Hello', True, 4.5]
    my_dict = {'first_name': 'Dave', 'lastname': 'Barcenas'}

    super_list = [
        {'first_name': 'Dave', 'lastname': 'Barcenas'},
        {'first_name': 'Raul', 'lastname': 'Torres'},
        {'first_name': 'Miguel', 'lastname': 'Rodelo'},
        {'first_name': 'Susana', 'lastname': 'MArtinez'}
    ]

    super_dict = {
        'natural_nums': [1, 2, 3, 4, 5],
        'integer_nums': [-1, -2, 0, 1, 2],
        'floating_nums': [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, '-', value)

    for item in super_list:
        print(item)
        

def run():
    list_comprehensions()    


if __name__ == '__main__':
    run()