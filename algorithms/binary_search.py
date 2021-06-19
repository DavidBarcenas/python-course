import random

def binary_search(list, start, end, objective):
    if start > end:
        return False;
    
    middle = (start + end) // 2

    if list[middle] == objective:
        return True
    elif list[middle] < objective:
        return binary_search(list, middle + 1, end, objective)
    else:
        return binary_search(list, start, middle - 1, objective)


if __name__ == '__main__':
    list_size = int(input('size list: '))
    objective = int(input('number to search: '))

    my_list = sorted([random.randint(0, 100) for i in range(list_size)])
    found = binary_search(my_list, 0, len(my_list), objective)

    print(my_list)
    print(f'item {objective} {"is in the list" if found else "not found"}')