import time

def factorial(n):
    response = 1

    while n > 1:
        response *= n
        n -= 1

    return response


def factorial_r(n):
    if n == 1:
        return 1

    return n * factorial_r(n - 1)


if __name__ == '__main__':
    n = 500

    start = time.time()
    factorial(n)
    end = time.time()
    print('time', end - start)
    
    start = time.time()
    factorial_r(n)
    end = time.time()
    print('time r', end - start)