import random

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def merge_and_sort_unique(list1, list2, list3, list4, ascending=True):
    unique_elements = set(list1) ^ set(list2) ^ set(list3) ^ set(list4)
    merged_and_sorted_list = sorted(list(unique_elements), reverse=not ascending)
    return merged_and_sorted_list


size = 15
list1 = [random.randint(-100, 100) for _ in range(size)]
list2 = [random.randint(-100, 100) for _ in range(size)]
list3 = [random.randint(-100, 100) for _ in range(size)]
list4 = [random.randint(-100, 100) for _ in range(size)]


sort_order = input("Введіть 'зр' для сортування за зростанням, 'сп' для сортування за спаданням: ").lower()
ascending = sort_order == 'зр'

merged_and_sorted_list = merge_and_sort_unique(list1, list2, list3, list4, ascending)

print("Об'єднані та унікальні елементи, відсортовані:", merged_and_sorted_list)


try:
    target_value = int(input("Введіть значення для бінарного пошуку: "))
except ValueError:
    print("Некоректний ввід для числа.")
    exit()

position = binary_search(merged_and_sorted_list, target_value)

if position != -1:
    print(f"Значення {target_value} знайдено на позиції {position}.")
else:
    print(f"Значення {target_value} не знайдено у списку.")