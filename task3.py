
# Задача №3:
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.

# Пример:
# 10 -> 1 2 4 8

n = int(input('-->  '))
print()

twoDegree = 0

poweredNumber = int()

while(poweredNumber < n):
    poweredNumber = 2 ** twoDegree
    print(f'2^{twoDegree} = {poweredNumber}')
    twoDegree += 1
    poweredNumber = 2 ** twoDegree

print()