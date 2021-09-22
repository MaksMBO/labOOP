import sys
from string import ascii_letters


def recursion(num_list, symbol, i):
    long = len(num_list)
    if i == long - 1 and not num_list[i].isalpha():
        return True
    else:
        if num_list[i].isdecimal():
            return recursion(num_list, symbol, i + 1)
        elif symbol.count(num_list[i]) == 1:
            if i <= long - 1 and symbol.count(num_list[i + 1]) == 1:
                return False
            elif symbol.count(num_list[long - 1]) == 1:
                return False
            else:
                return recursion(num_list, symbol, i + 1)
        else:
            return False


argument = sys.argv[1:]
i = 0
symbol = ('+', '-')

num_list = []
num = ''
if argument:
    for char in argument[0]:
        if char.isdigit() or char in ascii_letters:
            num += char
        else:
            if num != '':
                num_list.append(num)
                num = ''
            if symbol.count(char):
                num_list.append(char)
    if num != '':
        num_list.append(num)
else:
    num_list.append("a")

if recursion(num_list, symbol, i):
    print(f"({recursion(num_list, symbol, i)}, {eval(''.join(argument))})")
else:
    print(f"({recursion(num_list, symbol, i)}, {None})")
