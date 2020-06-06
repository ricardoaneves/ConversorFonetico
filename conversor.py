#!/usr/bin/python3

import time

# Vowels and consonants in the alphabet
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'w', 'x', 'y', 'z']

# IPA vowels
ipa_vowels = {'open a' : 'a',
              'closed a' : 'ɐ',
              'nasal a' : 'ɐ̃',
              'open e' : 'ɛ',
              'closed e' : 'ɛ',
              'mute e' : 'ɨ',
              'nasal e' : 'ẽ',
              'i' : 'i',
              'nasal i' : 'ĩ',
              'open o' : 'ɔ',
              'closed o' : 'o',
              'nasal o' : 'õ',
              'u' : 'u',
              'nasal u' : 'u'}

def get_syllables(word):

    array = list(word)
    res = []
    i = 0

    while i < len(array):

        # Sequências que formam ditongos decrescentes
        if (array[i] == 'a' and array[i+1] == 'i') or \
           (array[i] == 'a' and array[i+1] == 'u') or \
           (array[i] == 'á' and array[i+1] == 'u') or \
           (array[i] == 'ã' and array[i+1] == 'e') or \
           (array[i] == 'ã' and array[i+1] == 'i') or \
           (array[i] == 'ã' and array[i+1] == 'u'):

            res.append(array[i])
            res.append(array[i+1])
            res.append('.')
            i += 1

        # Sequências que formam ditongos decrescentes
        if (array[i] == 'e' and array[i+1] == 'i') or \
           (array[i] == 'e' and array[i+1] == 'u') or \
           (array[i] == 'é' and array[i+1] == 'i') or \
           (array[i] == 'é' and array[i+1] == 'u') or \
           (array[i] == 'ê' and array[i+1] == 'i'):

            res.append(array[i])
            res.append(array[i+1])
            res.append('.')
            i += 1

        # Sequências que formam ditongos decrescentes
        if array[i] == 'i' and array[i+1] == 'u':

            res.append(array[i])
            res.append(array[i+1])
            res.append('.')
            i += 1

        # Sequências que formam ditongos decrescentes
        if (array[i] == 'o' and array[i+1] == 'i') or \
           (array[i] == 'o' and array[i+1] == 'u') or \
           (array[i] == 'ó' and array[i+1] == 'i'):

            res.append(array[i])
            res.append(array[i+1])
            res.append('.')
            i += 1

        # Sequências que formam ditongos decrescentes
        if array[i] == 'u' and array[i+1] == 'i':

            res.append(array[i])
            res.append(array[i+1])
            res.append('.')
            i += 1

        # As combinações 'qu' e 'gu' não são separáveis da vogal ou ditongo que lhes sucede
        if (array[i] == 'q' and array[i+1] == 'u') or \
           (array[i] == 'g' and array[i+1] == 'u'):

            res.append(array[i])
            res.append(array[i+1])
            res.append(array[i+2])
            res.append('.')
            i += 2

        # Hiatos são indivisíveis quando ocorrem em silaba átona final
        if (array[i] == 'e' and array[i+1] == 'a') or \
           (array[i] == 'e' and array[i+1] == 'o') or \
           (array[i] == 'i' and array[i+1] == 'a') or \
           (array[i] == 'i' and array[i+1] == 'e') or \
           (array[i] == 'i' and array[i+1] == 'o') or \
           (array[i] == 'o' and array[i+1] == 'a') or \
           (array[i] == 'o' and array[i+1] == 'e') or \
           (array[i] == 'u' and array[i+1] == 'a') or \
           (array[i] == 'u' and array[i+1] == 'e') or \
           (array[i] == 'u' and array[i+1] == 'i') or \
           (array[i] == 'u' and array[i+1] == 'o'):


            if i == len(array)-2:
                
                res.append(array[i])
                res.append(array[i+1])
                res.append('.')
                i += 1
            
            else:
                i += 1

        i += 1

    syllables = ''.join(res)

    return syllables

if __name__ == '__main__':

    # Get word from standard input
    print('\n' + 'Insert word:')
    word = input()

    print('\n' + 'Processing word...')
    syllables = get_syllables(word)
    time.sleep(0.5)
    print()

    # Print results
    print('Plain word: ' + word)
    print('Stressed syllables: ' + syllables)
    print('IPA: ' + 'undefined' + '\n')