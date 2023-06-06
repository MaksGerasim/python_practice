# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8



def multip_a_b(a, b,):
    if b == 0:
        return 1
    return a * multip_a_b(a, b - 1)


a = int(input('A = '))
b = int(input('B = '))
c = multip_a_b(a, b)
print(c)

