def insertion_sort(list):
    for i in range(1, len(list)):
        current_value = list[i]
        current_position = i

        while current_position > 0 and list[current_position - 1] > current_value:
            list[current_position] = list[current_position - 1]
            current_position -= 1

        list[current_position] = current_value

    print(list)


if __name__ == '__main__':
    my_list = [3, 5, 9, 8, 7]
    insertion_sort(my_list)