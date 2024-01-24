def linear_search(product_list, target_product):
    for product, price in product_list:
        if product == target_product:
            return price
    return None

def binary_search_greater_equal(product_list, target_price):
    product_list.sort(key=lambda x: x[1])
    result_prices = []
    left, right = 0, len(product_list) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_price = product_list[mid][1]

        if mid_price >= target_price:
            result_prices.append(mid_price)
            right = mid - 1
        else:
            left = mid + 1

    return result_prices


products = [("яблуко", 2.5), ("банан", 1.8), ("апельсин", 3.0), ("виногран", 4.2), ("watermelon", 5.5)]

target_product = input("Введіть назву продукту для знаходження вартості: ")
linear_search_result = linear_search(products, target_product)

if linear_search_result is not None:
    print(f"Вартість продукту '{target_product}': {linear_search_result}")
else:
    print(f"Продукт '{target_product}' не знайдено.")

try:
    target_price = float(input("Введіть вартість продукту для знаходження всіх продуктів з більшою або рівною вартістю: "))
except ValueError:
    print("Некоректний ввід для вартості.")
    exit()

binary_search_result = binary_search_greater_equal(products, target_price)

if binary_search_result:
    print(f"Продукти з вартістю більше або рівної {target_price}: {binary_search_result}")
else:
    print(f"Продуктів з вартістю більше або рівної {target_price} не знайдено.")
