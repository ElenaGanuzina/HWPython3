# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000

def decimal_to_binary(num):
    res = []
    while num > 0:
        res.insert(0, num % 2)
        num //= 2
        
    print(*res, sep="")

num = int(input("n = "))
decimal_to_binary(num)