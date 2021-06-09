def useWhile():
    LIMIT = 10
    counter = 0

    while counter < LIMIT:
        print('Print', counter)
        counter += 1


def useFor():
    for counter in range(1, 1001):
        if counter % 2 != 0:
            continue
        print(counter)


def useBreak():
    for i in range(100):
        print(i)
        if( i == 56):
            break


def run():
    # name = input('Write your name: ')
    # for word in name:
    #     print(word)
    # phrase = input('Write a sentence')
    # for character in phrase:
    #     print(character.upper())
    useBreak()


if __name__ == '__main__':
    run()