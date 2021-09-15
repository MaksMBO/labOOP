import sys
from string import ascii_letters


def recursion(num_list, k, i):
    t = len(num_list)
    if i == t - 1:
        return True
    else:
        if num_list[i].isdecimal():
            return recursion(num_list, k, i + 1)
        elif k.count(num_list[i]) == 1:
            if i <= t - 1 and k.count(num_list[i + 1]) == 1:
                return False
            elif k.count(num_list[t - 1]) == 1:
                return False
            else:
                return recursion(num_list, k, i + 1)
        else:
            return False


argument = sys.argv[1:]
i = 0
k = ('+', '-')

num_list = []
num = ''
for char in argument[0]:
    if char.isdigit() or char in ascii_letters:
        num += char
    else:
        if num != '':
            num_list.append(num)
            num = ''
        if k.count(char):
            num_list.append(char)
if num != '':
    num_list.append(num)

if recursion(num_list, k, i):
    print(f"({recursion(num_list, k, i)}, {eval(''.join(argument))})")
else:
    print(f"({recursion(num_list, k, i)}, {None})")
