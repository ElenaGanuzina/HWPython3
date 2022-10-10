# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22

from random import sample

def create_list(num):
    my_list = sample(range(1, 50), num)
    return my_list

def odd_elements_sum(my_list: list):
    elements_sum = 0
    for i in range(0, len(my_list), 2):
        elements_sum += my_list[i]
    print(elements_sum)

my_list = create_list(int(input("n = ")))
print(my_list)
odd_elements_sum(my_list)

