def palindrome(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_reverse = palabra[::-1]
    if palabra == palabra_reverse:
        return(True)
    else:
        return(False)


def run():
    palabra = input('Escribe una palabra: ')
    es_palindrome = palindrome(palabra)
    if es_palindrome is True:
        print('Es palindrome')
    else:
        print('No es palindrome')

if __name__ == '__main__':
    run()
