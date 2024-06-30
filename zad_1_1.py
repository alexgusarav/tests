def check_age(age: int):

    if age > 18:
        result = 'Доступ разрешён'
    elif age <= 18:
        result = 'Доступ запрещён'

    return result


def check_month(month: int):
    if 0 < month <= 2: #or month == 12:
        result = "Зима"
    elif 2 < month <= 5:
        result = "Весна"
    elif 5 < month <= 8:
        result = "Лето"
    elif 8 < month <= 11:
        result = "Осень"
    else:
        result = "Некорректный номер месяца"
    return result


def check_triangle(side1: int, side2: int, side3: int):
    if side1 <= 0 or side2 <= 0 or side3 <= 0 or\
            (side1+side2) <= side3 or (side1+side3) <= side2 or (side3+side2) <= side1:
        result = "Треугольник не существует"
    elif side1 == side2 and side1 == side3:
        result = "Равносторонний треугольник"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        result = "Равнобедренный треугольник"
    else:
        result = "Разносторонний треугольник"
    return result