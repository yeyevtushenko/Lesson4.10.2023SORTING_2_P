import random

def linear_search_students(student_list, target_lastname):
    for i, student in enumerate(student_list):
        if student["lastname"] == target_lastname:
            return i

    return -1

names = ["Андрій", "Богдан", "Вікторія", "Галина", "Дмитро", "Євгенія", "Жанна", "Захар", "Ірина", "Катерина",
                   "Леонід", "Марія", "Наталія", "Олександр", "Павло", "Роман", "Софія", "Тарас", "Уляна", "Федір",
                   "Христина", "Цвітана", "Чеслав", "Шарлотта", "Щастя", "Юлія", "Ярослав", "Зеновій", "Альона"]

surnames = ["Іванов", "Петров", "Сидоров", "Коваленко", "Мельник", "Ковальчук", "Савченко", "Лисенко",
                      "Сергієнко", "Панасенко", "Бондаренко", "Кузнецов", "Олійник", "Кравчук", "Шевченко", "Козак",
                      "Марченко", "Василенко", "Ткаченко", "Костенко", "Міщенко", "Гриценко", "Зіновії", "Лесько",
                      "Данилюк", "Березенко", "Романченко", "Шевчук", "Медведенко"]

groups = ["БС-21", "БС-22", "БС-23", "БС-24", "БС-25"]

students = [{"firstname": name, "lastname": surname, "group": random.choice(groups)}
            for name, surname in zip(names, surnames)]

students.sort(key=lambda x: x['lastname'])

target_lastname = input("Введіть прізвище студента для пошуку: ")
position = linear_search_students(students, target_lastname)

if position != -1:
    print(f"Студента з прізвищем {target_lastname} знайдено на позиції {position}.")
else:
    print(f"Студента з прізвищем {target_lastname} не знайдено у списку.")
