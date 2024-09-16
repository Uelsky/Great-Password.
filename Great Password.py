from random import choice
import string


print('\n'.join([
    '1. Input length for new password',
    '2. Input invalid chars',
    '================================'
]))

password_len = int(input())
invalid_chars = input()

def key_generator(length: int, invalid_chars=''):
    if invalid_chars != '[]}{)(№?#_&$%@!,.':
        while length % 4 != 0:
            length += 1
        result = list()
        list_letters = [i for i in (string.ascii_letters + string.digits + '[]}{)(№?#_&$%@!,.')]
    else:
        while length % 3 != 0:
            length += 1
        result = list()
        list_letters = [i for i in (string.ascii_letters + string.digits)]


    def test_result(length, kwargs):
        test = kwargs
        control_count = length // 4
        up_count, low_count, dig_count, sign_count = 0, 0, 0, 0
        
        for i in test:
            if i.isupper():
                up_count += 1
            elif i.islower():
                low_count += 1
            elif i.isdigit():
                dig_count += 1
            else:
                sign_count += 1
                
        if (
            up_count == control_count
            and low_count == control_count
            and dig_count == control_count
            and sign_count <= control_count
        ):
            return False
        else:
            return True


    def test_char(char, invalid_chars, kwargs):
        if char in invalid_chars:
            return False
        test = kwargs
        control_count = length // 4
        up_count, low_count, dig_count, sign_count = 0, 0, 0, 0
        
        for i in test:
            if i.isupper():
                up_count += 1
            elif i.islower():
                low_count += 1
            elif i.isdigit():
                dig_count += 1
            else:
                sign_count += 1
                
        if char.isupper():
            up_count += 1
            if up_count > control_count:
                return False
            else:
                return True
                
        elif char.islower():
            low_count += 1
            if low_count > control_count:
                return False
            else:
                return True
                
        elif char.isdigit():
            dig_count += 1
            if dig_count > control_count:
                return False
            else:
                return True
                
        else:
            sign_count += 1
            if sign_count > control_count:
                return False
            else:
                return True


    while test_result(length, result):
        char = choice(list_letters)
        if test_char(char, invalid_chars, result):
            result.append(char)
        else:
            continue
    return "".join(result)


print(' '.join([
    'Your new password:',
    key_generator(password_len, invalid_chars)
]))
