#!/usr/bin/python3

import sys

# Vowels and consonants in the alphabet
vowels = ['a', 'e', 'i', 'o', 'u', 'á', 'à', 'ã', 'â', 'é', 'ê', 'í', 'ó', 'õ', 'ú', 'A', 'E', 'I', 'O', 'U', 'Á', 'À', 'Ã', 'Â', 'É', 'Ê', 'Í', 'Ó', 'Õ', 'Ú']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'ç', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z', 'Ç']

def get_syllables(text):

    array = list(text)
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

def ipa(text):

    array = list(text)
    res = []
    i = 0

    for i in range(len(array)):

        # Caracter especial
        if array[i] not in vowels and array[i] not in consonants:
            res.append(array[i])

        # Letra A
        if array[i] == 'a' or array[i] == 'á' or array[i] == 'à' or array[i] == 'â' or array[i] == 'ã' or \
           array[i] == 'A' or array[i] == 'Á' or array[i] == 'À' or array[i] == 'Â' or array[i] == 'Ã':

            if array[i] == 'á' or array[i] == 'à' or \
               array[i] == 'Á' or array[i] == 'À':
               
               res.append('a')
            
            elif array[i] == 'â' or array[i] == 'Â':
                res.append('ɐ')

            elif i < len(array)-1 and (array[i+1] == 'm' or array[i+1] == 'n' or \
                                       array[i+1] == 'M' or array[i+1] == 'N') :

                res.append('ɐ̃')

            elif array[i] == 'l' or array[i] == 'L':
                res.append('a')

            elif i < len(array)-1 and (array[i+1] == 'r' and array[i+2] == ' '):
                 res.append('a')

            else:
                res.append('ɐ')

        # Letra B
        if array[i] == 'b' or array[i] == 'B':
            res.append('b')

        # Letra C
        if array[i] == 'c' or array[i] == 'C':

            if i < len(array)-1 and (array[i+1] == 'a' or array[i+1] == 'A' or \
                                     array[i+1] == 'o' or array[i+1] == 'O' or \
                                     array[i+1] == 'u' or array[i+1] == 'U'):

               res.append('k')

            elif i < len(array)-1 and (array[i+1] == 'e' or array[i+1] == 'E' or \
                                       array[i+1] == 'i' or array[i+1] == 'I'):

                 res.append('s')

            elif i < len(array)-1 and (array[i+1] == 'h' or array[i+1] == 'H'):
                res.append('ʃ')

            else:
                res.append('k')

        # Letra Ç
        if array[i] == 'ç' or array[i] == 'Ç':
            res.append('s')

        # Letra D
        if array[i] == 'd' or array[i] == 'D':
            res.append('d')

        # Letra E
        if array[i] == 'e' or array[i] == 'é' or array[i] == 'ê' or \
           array[i] == 'E' or array[i] == 'É' or array[i] == 'Ê':

            if array[i] == 'é' or array[i] == 'É':
                res.append('ɛ')

            elif array[i] == 'ê' or array[i] == 'Ê':
                res.append('e')

            elif i < len(array)-1 and (array[i+1] == 'm' or array[i+1] == 'M' or \
                                       array[i+1] == 'n' or array[i+1] == 'n'):

                res.append('ẽ')

            elif i == 0:
                res.append('i')

            elif i == 1 and (array[i-1] == 'h' or array[i-1] == 'H'):
                res.append('i')

            elif (i > 0 or i < len(array)-1) and (array[i-1] in vowels or array[i+1] in vowels):
                res.append('i')

            else:
                res.append('ɨ')

        # Letra F
        if array[i] == 'f' or array[i] == 'F':
            res.append('f')

        # Letra G
        if array[i] == 'g' or array[i] == 'G':

            if i < len(array)-1 and (array[i+1] == 'e' or array[i+1] == 'E' or \
                                     array[i+1] == 'i' or array[i+1] == 'I'):

                res.append('ʒ')
            
            else:
                res.append('g')

        # Letra H
        if array[i] == 'h' or array[i] == 'H':
            continue

        # Letra I
        if array[i] == 'i' or array[i] == 'I':

            if i < len(array)-1 or (array[i+1] == 'm' or array[i+1] == 'M' or\
                                    array[i+1] == 'n' or array[i+1] == 'N'):
                res.append('ĩ')
            
            else:
                res.append('i')
            
        # Letra J
        if array[i] == 'j' or array[i] == 'J':
            res.append('ʒ')

        # Letra K
        if array[i] == 'k' or array[i] == 'K':
            res.append('k')

        # Letra L
        if array[i] == 'l' or array[i] == 'L':

            if i < len(array)-1 or (array[i+1] == 'h' or array[i+1] == 'H'):
                res.append('ʎ')
            
            else:
                res.append('l')

        # Letra M
        if array[i] == 'm' or array[i] == 'M':

            if i > 0 and array[i-1] == 'i':
                continue
            
            else:
                res.append('m')

        # Letra N
        if array[i] == 'n' or array[i] == 'N':

            if i < len(array)-1 and (array[i+1] == 'h' or array[i+1] == 'H'):
                res.append('ɲ')

            else:
                res.append('n')

    ipa = ''.join(res)

    return ipa

if __name__ == '__main__':

    if len(sys.argv) > 2:
        print('\n' + 'Wrong input format, please try again:')
        print('python3 conversor.py \'<TEXT>\'' + '\n')
        sys.exit()

    # Get words from standard input
    words = sys.argv

    words.pop(0)
    text = ' '.join(words)

    print('\n' + 'Processing text...')
    syllables = get_syllables(text)
    ipa = ipa(syllables)
    print()

    # Print results
    print('Number of words: ' + str(len(text.split(' '))))
    print('Plain text: ' + text)
    print('Stressed syllables: ' + syllables)
    print('IPA: ' + ipa)
    print('X-SAMPA: ' + 'undefined' + '\n')