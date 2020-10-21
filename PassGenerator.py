from random import *

def generate_password(len_pass, l_chars):
    g_pass = []
    for _ in range(int(len_pass)):
        g_pass.append(choice(l_chars))
    print(*g_pass, sep='')


def game():
    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = "'!#$%&*+-=?@^_"
    chars = ''
    print('How much passwords you need?')
    num_pass = input()
    print('How much symbols you need?')
    len_pass = input()
    print('Включать ли цифры 0123456789? (y/n)')
    pass_digit = input()
    if pass_digit == 'y':
        pass_digit = True
    else:
        pass_digit = False
    print('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n)')
    pass_alpha_up = input()
    if pass_alpha_up == 'y':
        pass_alpha_up = True
    else:
        pass_alpha_up = False
    print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n)')
    pass_alpha_low = input()
    if pass_alpha_low == 'y':
        pass_alpha_low = True
    else:
        pass_alpha_low = False
    print('Включать ли символы !#$%&*+-=?@^_? (y/n)')
    pass_symbols = input()
    if pass_symbols == 'y':
        pass_symbols = True
    else:
        pass_symbols = False
    print('Исключать ли неоднозначные символы il1Lo0O? (y/n)')
    pass_strange_symbols = input()
    if pass_strange_symbols == 'y':
        pass_strange_symbols = True
    else:
        pass_strange_symbols = False

    if pass_digit:
        chars += digits
    if pass_alpha_up:
        chars += uppercase_letters
    if pass_alpha_low:
        chars += lowercase_letters
    if pass_symbols:
        chars += punctuation
    l_chars = list(chars)
    if pass_strange_symbols:
        if pass_digit:
            l_chars.remove('0')
            l_chars.remove('1')
        if pass_alpha_up:
            l_chars.remove('L')
            l_chars.remove('O')
        if pass_alpha_low:
            l_chars.remove('i')
            l_chars.remove('l')
            l_chars.remove('o')

    for _ in range(int(num_pass)):
        generate_password(len_pass, l_chars)

game()
