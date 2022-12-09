import time
import random
import string
from matplotlib import pyplot as plt
from multiprocessing import Pool


alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
d = 20


def caesar_cipher(message):
    result = ''
    for i in message:
        j = alphabet.find(i)
        l = (j + d - 1) % 26 + 1
        if i in alphabet:
            result += alphabet[l]
        else:
            result += i
    return result


def random_word(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length)).upper()


def random_sentence(word_count):
    length = word_count
    return ' '.join(random_word(length) for i in range(word_count))


def sp_method(message):
    start_time = time.time()
    print(caesar_cipher(message))
    execution_time = time.time() - start_time
    print(f'Single process execution time ---> {execution_time} sec <---')
    return execution_time


def mp_method(message):
    start_time2 = time.time()
    with Pool() as p:
        print(p.map(caesar_cipher, message))
    execution_time2 = time.time() - start_time2
    print(f'Multiprocessing execution time ---> {execution_time2} sec <---')
    return execution_time2


if __name__ == '__main__':
    tests = [2 ** n for n in range(1, 14)]
    res = []
    res2 = []

    for test in tests:
        print(f'||| TESTS {test} |||')
        message = random_sentence(test)
        print('Single process text: ', message)

        res.append(sp_method(message))
        print('\n')

        message2 = message.split(' ')
        print('Multiprocessing string list: ', message2)

        res2.append(mp_method(message2))

    plt.plot(tests, res, color='green')
    plt.plot(tests, res2, color='blue')
    plt.show()
