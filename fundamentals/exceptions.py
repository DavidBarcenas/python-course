def spli_list(list, divider):
    try:
        return [i / divider for i in list]
    except ZeroDivisionError as e:
        print(e)
        return list

new_list = list(range(10))
divider = 0

print(spli_list(new_list, divider))