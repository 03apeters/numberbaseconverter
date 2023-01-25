# Converts between any base
# from base-2 to base-36
#
# Anthony R Peters
#

import math

def main():
    startbase = input('Enter a base to convert from (int in base-10): ')
    endbase = input('Enter a base to convert to (int in base-10): ')
    number = input('Enter the number to convert: ')
    print(f'the number {number} in base-{startbase} is {convertany(startbase, endbase, number)} in base-{endbase}')

def convertany(startbase, endbase, number):
    return tentoanybase(int(endbase), anybasetoten(int(startbase), number))


def tentoanybase(base, number):
    '''
    :param base: an int representing the end numbers base
    :param number: a base 10 int to be converted
    :return: an int in the given base
    '''

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    newNum = ''
    while number != 0:
        newNum += digits[number%base]
        number = math.floor(number/base)
    return newNum[::-1]


def anybasetoten(base, number):
    '''
    :param base: the base of the int
    :param number: the number given in entered base
    :return: the given int converted to base 10
    '''
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    characters = characters[0:(base-10)]
    digits = dict()
    for i in range(len(characters)):
        digits[characters[i]] = 10 + i
    decimal = 0
    number = str(number)
    number = number[::-1]
    for i in range(len(number)):
        if number[i].isalpha():
            try:
                digit = digits[number[i].upper()]
            except KeyError:
                print(f'{number[i]} is an invalid digit in base-{base}')
                exit()
        else:
            digit = number[i]
        decimal += (base**i) * int(digit)
    return decimal


main()