#!/usr/bin/python

import string

def decimal_to_binary(number):
    binary = ''
   
    if number < 0:
        raise ValueError

    if number == 0:
        return '0'

    while number > 0:
        binary = str(number % 2) + binary
        number = number >> 1

    return binary

def on_or_off(n, k):
    if decimal_to_binary(k)[-n:] == '1' * n:
        return 'ON'

    return 'OFF'

def process_input(input, output):
    for i in range(int(input.readline())):
        n, k = map(lambda s: int(s), input.readline().split(' '))
        output.write('Case #%d: %s\n' % (i + 1, on_or_off(n, k)))

def main():
    input = open('snapper_chain.in', 'r')
    output = open('snapper_chain.out', 'w')

    process_input(input, output)

    input.close()
    output.close()
 
if __name__ == '__main__':
    main()

