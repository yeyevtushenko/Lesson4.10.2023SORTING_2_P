def binary_search(countries, target):
    low, high = 0, len(countries) - 1

    while low <= high:
        mid = (low + high) // 2
        if countries[mid] == target:
            return mid
        elif countries[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


sorted_countries = ["Australia", "Brazil", "Canada", "China", "Egypt", "France", "Germany", "India", "Italy", "Japan",
                    "Mexico", "Norway", "South Africa", "Spain", "Sweden", "Switzerland", "United Kingdom",
                    "United States", "Ukraine", "Vietnam", "Zimbabwe", "Argentina", "Chile", "Colombia", "Peru"]

try:
    target_country = input(f"Введіть назву країни для пошуку у списку\n{sorted_countries}: ")
except ValueError:
    print("Некоректний ввід для назви країни.")
    exit()

position = binary_search(sorted_countries, target_country)

if position != -1:
    print(f"Країну {target_country} знайдено на позиції {position}.")
else:
    print(f"Країну {target_country} не знайдено у списку.")
