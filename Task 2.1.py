import random

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def merge_and_sort(list1, list2, list3, list4, ascending=True):
    merged_list = list1 + list2 + list3 + list4
    merged_list.sort(reverse=not ascending)
    return merged_list


size = 25
list1 = [random.randint(-100, 100) for _ in range(size)]
list2 = [random.randint(-100, 100) for _ in range(size)]
list3 = [random.randint(-100, 100) for _ in range(size)]
list4 = [random.randint(-100, 100) for _ in range(size)]


sort_order = input("Введіть 'зр' для сортування за зростанням,'сп' для сортування за спаданням: ").lower()
ascending = sort_order == "зр"


merged_and_sorted_list = merge_and_sort(list1, list2, list3, list4, ascending)

print("Об'єднаний та відсортований список:", merged_and_sorted_list)


try:
    target_value = int(input("Введіть значення для лінійного пошуку: "))
except ValueError:
    print("Некоректний ввід для числа.")
    exit()


position = linear_search(merged_and_sorted_list, target_value)

if position != -1:
    print(f"Значення {target_value} знайдено на позиції {position}.")
else:
    print(f"Значення {target_value} не знайдено у списку.")