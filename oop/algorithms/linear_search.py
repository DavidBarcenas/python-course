import random

def linear_search(list, objective):
    match = False;

    for i in list: # O(n)
        if i == objective:
            match = True
            break

    return match


if __name__ == '__main__':
    list_size = int(input('size list: '))
    objective = int(input('number to search: '))

    my_list = [random.randint(0, 100) for i in range(list_size)]
    found = linear_search(my_list, objective)

    print(my_list)
    print(f'item {objective} {"is in the list" if found else "not found"}')