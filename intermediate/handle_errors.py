def palindrome_assert(string):
    assert len(string) > 0, 'Cannot enter an empty string'
    return string == string[::-1]


def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError('Cannot enter an empty string')
        return string == string[::-1]
    except ValueError as err:
        print(err)
        return False


def divisors(num):
    divisors = []

    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)

    return divisors


def run():
    try:
       print(palindrome(''))
    except TypeError:
        print('Only strings can be entered')


if __name__ == '__main__':
    run()