# Raindrops - Exercism
'''Convert a number to a string, depending on the number's factors.
    If it has 3 as a factor, output 'Pling', 5: 'Plang', 7: 'Plong'.
    If it has none of them, pass the number's digits straight through.'''
from collections import namedtuple
Noises = namedtuple('Noises', 'factor string')
NOISE_LIST = [Noises(3, 'Pling'),
    Noises(5, 'Plang'),
    Noises(7, 'Plong')]
def raindrops(number):
    output = ''
    for noise in NOISE_LIST:
        if number % noise.factor == 0:
            output += noise.string
    return output if output else str(number)
if __name__ == '__main__':
    print(raindrops(21))
    print(raindrops(1))