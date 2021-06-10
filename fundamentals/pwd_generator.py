import random

def pwd_generator():
    upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbols = ['!', '#', '*', '$', '/', '(', ')']

    characters = upper_case + lower_case + nums + symbols
    new_pwd = []

    for i in range(15):
        random_character = random.choice(characters)
        new_pwd.append(random_character)

    new_pwd = ''.join(new_pwd)
    return new_pwd


def run():
    pwd = pwd_generator()
    print('Your new password is:', pwd)


if __name__ == '__main__':
    run()