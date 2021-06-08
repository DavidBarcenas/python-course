def palindrome(word):
    word = word.replace(' ', '').lower()
    inverted_word = word[::-1]
    return word == inverted_word;


def run():
    word = input('Write a word: ')
    is_palindrome = palindrome(word)

    if is_palindrome == True:
        print('Is palindrome')
    else:
        print('It is not palindrome')


if __name__ == '__main__':
    run()