import random

def mix_sort(list):
    if len(list) > 1:
        half = len(list) // 2
        left = list[:half] # from zero to half
        right = list[half:] # from the middle to the end

        print(left, '*' * 5, right)

        # recursive call in each half
        mix_sort(left)
        mix_sort(right)

        # iterators to loop through the two sublists
        i = 0
        j = 0
        # iterator for main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1

        print(f'left {left}, right {right}')
        print(list)
        print('-' * 50)

    return list


if __name__ == '__main__':
    list_size = int(input('Size list: '))
    my_list = [random.randint(0, 100) for i in range(list_size)]

    print(my_list)
    print('-' * 20)

    order_list = mix_sort(my_list)
    print(order_list)