def primality(num):
    counter = 0

    for i in range(1, num + 1):
        if i == 1 or i == num:
            continue
        if num % 1 == 0:
            counter += 1

    return counter == 0


def run():
    num = int(input('Write a number: '))
    if primality(num):
        print('Is prime number')
    else:
        print('it is not a prime number')


if __name__ == '__main__':
    run()