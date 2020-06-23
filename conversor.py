#!/usr/bin/python3

import sys
import json

# Vowels and consonants in the alphabet
vowels = ['a', 'e', 'i', 'o', 'u', 'á', 'à', 'ã', 'â', 'é', 'ê', 'í', 'ó', 'õ', 'ô', 'ú', 'A', 'E', 'I', 'O', 'U', 'Á', 'À', 'Ã', 'Â', 'É', 'Ê', 'Í', 'Ó', 'Õ', 'Ô', 'Ú']
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
                res.append('·')
                flag = 1

        # As combinações 'qu' e 'gu' não são separáveis da vogal ou ditongo que lhes sucede
        if (array[i] == 'q' and array[i+1] == 'u') or \
           (array[i] == 'g' and array[i+1] == 'u'):

            if i != 0:
                res.append('·')

            res.append(array[i])
            res.append(array[i+1])
            i += 1
            flag = 1

        # Consoantes seguidas de vogais permanecem em inicio da silaba (ataque)
        elif array[i] in consonants and array[i+1] in vowels:

            if i != 0:
                res.append('·')

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
                    res.append('·')
                    
                res.append(array[i])
                res.append(array[i+1])
                i += 1
                flag = 1
            
            # Digrafos - sequencias de consoantes que representam um só som não se separam
            if  (array[i] == 'c' and array[i+1] == 'h') or \
                (array[i] == 'l' and array[i+1] == 'h') or \
                (array[i] == 'n' and array[i+1] == 'h'):

                if i != 0:
                    res.append('·')

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
            if res[i+1] == '·':
                res[i+1] = ''

    syllables = ''.join(res)

    return syllables

def get_stressed(text):

    stressed = ''

    

    return stressed

def get_ipa(text):

    array = list(text)
    res = []
    i = 0

    for i in range(len(array)):

        # Caracter especial
        if array[i] not in vowels and array[i] not in consonants:

            if array[i] == '·':
                res.append('.')

            else:
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

            elif (i > 0 and array[i-1] in vowels) or (i < len(array)-1 and array[i+1] in vowels):
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
        if array[i] == 'i' or array[i] == 'í' or \
           array[i] == 'I' or array[i] == 'Í':

            if i < len(array)-1 and (array[i+1] == 'm' or array[i+1] == 'M' or\
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

            if i < len(array)-1 and (array[i+1] == 'h' or array[i+1] == 'H'):
                res.append('ʎ')
            
            else:
                res.append('l')

        # Letra M
        if array[i] == 'm' or array[i] == 'M':

            if (i == len(array)-1 or array[i+1] == ' ') and (array[i-1] == 'a' or array[i-1] == 'A'):
                res.append('w')

            elif (i == len(array)-1 or array[i+1] == ' ') and (array[i-1] == 'e' or array[i-1] == 'E'):
                res.append('j')
            
            else:
                res.append('m')

        # Letra N
        if array[i] == 'n' or array[i] == 'N':

            if i > 0 and array[i-1] in vowels:
                continue

            elif i < len(array)-1 and (array[i+1] == 'h' or array[i+1] == 'H'):
                res.append('ɲ')

            else:
                res.append('n')

        # Letra O
        if array[i] == 'o' or array[i] == 'ó' or array[i] == 'ô' or array[i] == 'õ' or \
           array[i] == 'O' or array[i] == 'Ó' or array[i] == 'Ô' or array[i] == 'Õ':

            if array[i] == 'ó' or array[i] == 'Ó':
                res.append('ɔ')

            elif array[i] == 'ô' or array[i] == 'Ô':
                res.append('o')

            elif array[i] == 'õ' or array[i] == 'Õ':
                res.append('õ')

            elif i == 0:
                res.append('ɔ')

            elif i == 1 and (array[i-1] == 'h' or array[i-1] == 'H'):
                res.append('ɔ')

            elif i < len(array)-1 and (array[i+1] == 'm' or array[i+1] == 'n' or \
                                       array[i+1] == 'M' or array[i+1] == 'N') :

                res.append('õ')

            else:
                res.append('u')

        # Letra P
        if array[i] == 'p' or array[i] == 'P':
            res.append('p')

        # Letra Q
        if array[i] == 'q' or array[i] == 'Q':
            res.append('k')

        # Letra R
        if array[i] == 'r' or array[i] == 'R':

            if i < len(array)-1 and (array[i+1] == 'r' or array[i+1] == 'R'):
                res.append('ʁ')

            elif i > 0 and (array[i-1] == 'r' or array[i-1] == 'R'):
                continue

            elif i == 0:
                res.append('ʁ')

            else:
                res.append('ɾ')

        # Letra S
        if array[i] == 's' or array[i] == 'S':

            if i == 0:
                res.append('s')

            elif i == len(array)-1:
                res.append('ʃ')

            elif i < len(array)-1 and (array[i+1] == 's' or array[i+1] == 'S'):
                res.append('s')
            
            elif i > 0 and (array[i-1] == 's' or array[i-1] == 'S'):
                continue

            elif i < len(array)-1 and (array[i+1] == 'c' or array[i+1] == 'ç' or array[i+1] == 'f' or array[i+1] == 'p' or array[i+1] == 'q' or array[i+1] == 's' or array[i+1] == 't' or array[i+1] == ' ' or \
                                       array[i+1] == 'C' or array[i+1] == 'Ç' or array[i+1] == 'F' or array[i+1] == 'P' or array[i+1] == 'Q' or array[i+1] == 'S' or array[i+1] == 'T'):
                res.append('ʃ')

            elif i < len(array)-1 and (array[i+1] == 'b' or array[i+1] == 'd' or array[i+1] == 'g' or array[i+1] == 'j' or array[i+1] == 'l' or array[i+1] == 'm' or array[i+1] == 'n' or array[i+1] == 'r' or array[i+1] == 'v' or array[i+1] == 'z' or array[i+1] == ' ' or \
                                       array[i+1] == 'B' or array[i+1] == 'D' or array[i+1] == 'G' or array[i+1] == 'J' or array[i+1] == 'L' or array[i+1] == 'M' or array[i+1] == 'N' or array[i+1] == 'R' or array[i+1] == 'V' or array[i+1] == 'Z'):
                res.append('ʒ')

            elif (i > 0 or i < len(array)-1) and (array[i-1] in vowels or array[i+1] in vowels):
                res.append('z')

            else:
                res.append('s')
            
        # Letra T
        if array[i] == 't' or array[i] == 'T':
            res.append('t')

        # Letra U
        if array[i] == 'u' or array[i] == 'ú' or \
           array[i] == 'U' or array[i] == 'Ú':

            if i < len(array)-1 and (array[i+1] == 'm' or array[i+1] == 'M' or \
                                     array[i+1] == 'n' or array[i+1] == 'n'):

                res.append('ũ')
            
            else:
                res.append('u')

        # Letra V
        if array[i] == 'v' or array[i] == 'V':
            res.append('v')

        # Letra W
        if array[i] == 'w' or array[i] == 'W':
            res.append('u')

        # Letra X
        if array[i] == 'x' or array[i] == 'X':

            if i == 0:
                res.append('ʃ')

            elif i > 1 and ((array[i-2] == 'm' or array[i-2] == 'M') and (array[i-1] == 'e' or array[i-1] == 'E')):
                res.append('ʃ')

            elif i > 1 and ((array[i-2] == 'e' or array[i-2] == 'E') and (array[i-1] == 'n' or array[i-1] == 'N')):
                res.append('ʃ')

            elif i > 1 and array[i-2] in vowels and array[i-1] in vowels:
                res.append('ʃ')

            else:
                res.append('z')

        # Letra Y
        if array[i] == 'y' or array[i] == 'Y':
            res.append('i')

        # Letra Z
        if array[i] == 'z' or array[i] == 'Z':

            if i == 0:
                res.append('z')

            elif i == len(array)-1:
                res.append('ʃ')

            elif i < len(array)-1 and (array[i+1] == 'c' or array[i+1] == 'ç' or array[i+1] == 'f' or array[i+1] == 'p' or array[i+1] == 'q' or array[i+1] == 's' or array[i+1] == 't' or array[i+1] == ' ' or \
                                       array[i+1] == 'C' or array[i+1] == 'Ç' or array[i+1] == 'F' or array[i+1] == 'P' or array[i+1] == 'Q' or array[i+1] == 'S' or array[i+1] == 'T'):
                res.append('ʃ')

            elif i < len(array)-1 and (array[i+1] == 'b' or array[i+1] == 'd' or array[i+1] == 'g' or array[i+1] == 'j' or array[i+1] == 'l' or array[i+1] == 'm' or array[i+1] == 'n' or array[i+1] == 'r' or array[i+1] == 'v' or array[i+1] == 'z' or array[i+1] == ' ' or \
                                       array[i+1] == 'B' or array[i+1] == 'D' or array[i+1] == 'G' or array[i+1] == 'J' or array[i+1] == 'L' or array[i+1] == 'M' or array[i+1] == 'N' or array[i+1] == 'R' or array[i+1] == 'V' or array[i+1] == 'Z'):
                res.append('ʒ')

            elif (i > 0 or i < len(array)-1) and (array[i-1] in vowels or array[i+1] in vowels):
                res.append('z')

            else:
                res.append('z')

    ipa = ''.join(res)

    return ipa

def get_solution(text):

    res = []

    with open('ipa.json') as ipa:
        data = json.load(ipa)

    text = text.split(' ')
    for word in text:
        for w in data:
            if word == w[0]:
                res.append(w[1])
                res.append(' ')

    ipa.close()

    if len(res) > 0:
        res.pop()

    solution = ''.join(res)

    return solution

def get_percentage(ipa, solution):

    corrects = 0
    chars = 0
    i = 0

    ipa = list(ipa)
    solution = list(solution)

    solution = [j for j in solution if j != 'ˈ']

    if len(ipa) > len(solution):
        length = len(solution)
    else:
        length = len(ipa)

    print(ipa)
    print(solution)

    while i < length:

        chars += 1
        if ipa[i] == solution[i]:
            print(ipa[i])
            print(solution[i])
            print()
            corrects += 1

        i += 1 

    if chars == 0:
        chars = 1

    percentage = corrects / chars * 100

    return [percentage, corrects, chars]

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
    stressed = get_stressed(syllables)
    ipa = get_ipa(syllables)
    solution = get_solution(syllables)
    triple = get_percentage(ipa, solution)
    print()

    # Print results
    print('Number of words: ' + str(len(text.split(' '))))
    print('Plain text: ' + text)
    print('Stressed syllables: ' + syllables)
    print('IPA: ' + ipa)
    print('Solution: ' + solution)
    print('Correct chars: ' + str(triple[1]) + '/' + str(triple[2]) + ', ' + ('%.2f' % triple[0]) + '%' + '\n')