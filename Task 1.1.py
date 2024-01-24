import random

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1


size = random.randint(5, 25)
random_list = [random.randint(-100, 100) for _ in range(size)]

try:
    target_number = int(input(f"Введіть число для пошуку у списку {random_list}: "))
except ValueError:
    print("Некоректний ввід для числа.")
    exit()

position = linear_search(random_list, target_number)

if position != -1:
    print(f"Число {target_number} знайдено на позиції {position}.")
else:
    print(f"Число {target_number} не знайдено у списку.")
