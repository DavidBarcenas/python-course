PASSWORD = 'secret123'

def password_required(func):
    def wrapper():
        password = input('What is your password? ')

        if password == PASSWORD:
            return func()
        else:
            print('The password is not correct')

    return wrapper


@password_required
def needs_password():
    print('The password is correct!')


def upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper

@upper
def say_hello(name):
    return f'Hello {name}'


if __name__ == '__main__':
    print(say_hello('David'))