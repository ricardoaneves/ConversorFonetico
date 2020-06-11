#!/usr/bin/python3

import time

# Vowels and consonants in the alphabet
vowels = ['a', 'e', 'i', 'o', 'u', 'á', 'à', 'ã', 'â', 'é', 'ẽ', 'ê', 'í', 'ó', 'õ', 'ú', 'A', 'E', 'I', 'O', 'U']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'ç']

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
              'nasal u' : 'ũ'}

def get_syllables(word):

    array = list(word)
    res = []
    i = 0

    while i < len(array)-1:

        flag = 0

        # Prefixos que terminam em b e d
        if i == 0:
            if (array[i] == 's' and array[i+1] == 'u' and array[i+2 == 'b']):

                res.append(array[i])
                res.append(array[i+1])
                res.append(array[i+2])
                i += 2
                flag = 1

            elif (array[i] == 'a' and array[i+1] == 'b') or \
                (array[i] == 'a' and array[i+1] == 'd'):

                res.append(array[i])
                res.append(array[i+1])
                i += 1
                flag = 1

        # Hiatos e vogais duplas dividem-se em duas silabas diferentes
        if array[i] in vowels and array[i+1] in vowels:

            # Sequências que formam ditongos decrescentes
            if (array[i] == 'a' and array[i+1] == 'i') or \
               (array[i] == 'a' and array[i+1] == 'u') or \
               (array[i] == 'á' and array[i+1] == 'u') or \
               (array[i] == 'ã' and array[i+1] == 'e') or \
               (array[i] == 'ã' and array[i+1] == 'i') or \
               (array[i] == 'ã' and array[i+1] == 'o'):

                res.append(array[i])
                flag = 1

            # Sequências que formam ditongos decrescentes
            elif (array[i] == 'e' and array[i+1] == 'i') or \
                 (array[i] == 'e' and array[i+1] == 'u') or \
                 (array[i] == 'é' and array[i+1] == 'i') or \
                 (array[i] == 'é' and array[i+1] == 'u') or \
                 (array[i] == 'ê' and array[i+1] == 'i'):

                res.append(array[i])
                flag = 1

            # Sequências que formam ditongos decrescentes
            elif array[i] == 'i' and array[i+1] == 'u':

                res.append(array[i])
                flag = 1

            # Sequências que formam ditongos decrescentes
            elif (array[i] == 'o' and array[i+1] == 'i') or \
                 (array[i] == 'o' and array[i+1] == 'u') or \
                 (array[i] == 'ó' and array[i+1] == 'i'):

                res.append(array[i])
                flag = 1

            # Sequências que formam ditongos decrescentes
            elif array[i] == 'u' and array[i+1] == 'i':

                res.append(array[i])
                flag = 1

            # Hiatos são indivisíveis quando ocorrem em silaba átona final
            elif ((array[i] == 'e' and array[i+1] == 'a') or \
                  (array[i] == 'e' and array[i+1] == 'o') or \
                  (array[i] == 'i' and array[i+1] == 'a') or \
                  (array[i] == 'i' and array[i+1] == 'e') or \
                  (array[i] == 'i' and array[i+1] == 'o') or \
                  (array[i] == 'o' and array[i+1] == 'a') or \
                  (array[i] == 'o' and array[i+1] == 'e') or \
                  (array[i] == 'u' and array[i+1] == 'a') or \
                  (array[i] == 'u' and array[i+1] == 'e') or \
                  (array[i] == 'u' and array[i+1] == 'i') or \
                  (array[i] == 'u' and array[i+1] == 'o')) and \
                  i == len(array)-2:
                    
                res.append(array[i])
                flag = 1

            else:

                res.append(array[i])
                res.append('.')
                flag = 1

        # As combinações 'qu' e 'gu' não são separáveis da vogal ou ditongo que lhes sucede
        if (array[i] == 'q' and array[i+1] == 'u') or \
           (array[i] == 'g' and array[i+1] == 'u'):

            if i != 0:
                res.append('.')

            res.append(array[i])
            res.append(array[i+1])
            i += 1
            flag = 1

        # Consoantes seguidas de vogais permanecem em inicio da silaba (ataque)
        elif array[i] in consonants and array[i+1] in vowels:

            if i != 0:
                res.append('.')

            res.append(array[i])
            flag = 1

        # Consoantes seguidas de outra consoante permanecem em final de silaba
        if array[i] in consonants and array[i+1] in consonants and flag == 0:

            # Grupos consonanticos não são divisiveis
            if (array[i] == 'b' and array[i+1] == 'l') or \
               (array[i] == 'b' and array[i+1] == 'r') or \
               (array[i] == 'c' and array[i+1] == 'l') or \
               (array[i] == 'c' and array[i+1] == 'r') or \
               (array[i] == 'd' and array[i+1] == 'l') or \
               (array[i] == 'd' and array[i+1] == 'r') or \
               (array[i] == 'f' and array[i+1] == 'l') or \
               (array[i] == 'f' and array[i+1] == 'r') or \
               (array[i] == 'g' and array[i+1] == 'l') or \
               (array[i] == 'g' and array[i+1] == 'r') or \
               (array[i] == 'p' and array[i+1] == 'l') or \
               (array[i] == 'p' and array[i+1] == 'r') or \
               (array[i] == 't' and array[i+1] == 'l') or \
               (array[i] == 't' and array[i+1] == 'r') or \
               (array[i] == 'v' and array[i+1] == 'l') or \
               (array[i] == 'v' and array[i+1] == 'r'):

                if i != 0:
                    res.append('.')
                    
                res.append(array[i])
                res.append(array[i+1])
                i += 1
                flag = 1
            
            # Digrafos - sequencias de consoantes que representam um só som não se separam
            if  (array[i] == 'c' and array[i+1] == 'h') or \
                (array[i] == 'l' and array[i+1] == 'h') or \
                (array[i] == 'n' and array[i+1] == 'h'):

                if i != 0:
                    res.append('.')

                res.append(array[i])
                res.append(array[i+1])
                i += 1
                flag = 1

            # Sao indivisiveis os grupos consonanticos cz e ps em inicio de palavra
            if i == 0:

                if (array[i] == 'c' and array[i+1] == 'z') or \
                   (array[i] == 'p' and array[i+1] == 's'):

                    res.append(array[i])
                    res.append(array[i+1])
                    i += 1
                    flag = 1

        # Se nenhuma regra foi aceite
        if flag == 0:
            res.append(array[i])

        i += 1
        
    res.append(array[i])

    for i in range(len(res)):
    
        if res[i] == ' ':
            if res[i+1] == '.':
                res[i+1] = ''

    syllables = ''.join(res)

    return syllables

if __name__ == '__main__':

    # Get word from standard input
    print('\n' + 'Insert word:')
    word = input()

    print('\n' + 'Processing word...')
    syllables = get_syllables(word)
    print()

    # Print results
    print('Plain word: ' + word)
    print('Stressed syllables: ' + syllables)
    print('IPA: ' + 'undefined' + '\n')