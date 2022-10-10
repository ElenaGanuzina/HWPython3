# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]


from random import sample

def create_list(num):
    my_list = sample(range(10), k = num)
    return my_list

def multiply_elements(my_list):
    length = len(my_list)
    new_list = []
    
    for i in range(length//2):
        new_list.append(my_list[i] * my_list[length - 1 - i])
    if length % 2 != 0:
        new_list.append(my_list[length // 2])
    print(new_list)


my_list = create_list(int(input("n = ")))
print(my_list)
multiply_elements(my_list)