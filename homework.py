# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 списка. 1 строка - первый список через пробел. 2 строка - второй список через пробел.

def sort_inter_list(*lists):
    s = {}
    for item in lists:
        if len(s):
            s = set.intersection(s, set(item))
        else:
            s = set(item)   
    return sorted(list(s))

list1 = map(int, input("Введите 1-ый массив: ").split(" "))
list2 = map(int, input("Введите 2-ой массив: ").split(" "))

print(sort_inter_list(list1, list2))