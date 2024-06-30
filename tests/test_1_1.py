import pytest
from zad_1_1 import check_age, check_month, check_triangle


@pytest.mark.parametrize(
    'age,answer',
    (
        [16, 'Доступ запрещён'],
        [18, 'Доступ разрешён'],
        [19, 'Доступ разрешён'],
    )
)
def test_zad_1_1(age, answer):
    result = check_age(age)
    assert result == answer


@pytest.mark.parametrize(
    'month,answer',
    (
        [1, 'Зима'],
        [12, 'Зима'],
        [4, 'Весна'],
        [7, 'Лето'],
        [13, 'Некорректный номер месяца'],
    )
)
def test_zad_1_2(month, answer):
    result = check_month(month)
    assert result == answer


@pytest.mark.parametrize(
    'side1,side2,side3,answer',
    (
        [1, 2, 3, "Треугольник не существует"],
        [1, -2, 3, "Треугольник не существует"],
        [1, 1, 1, 'Равносторонний треугольник'],
        [2, 2, 3, 'Равнобедренный треугольник'],
        [7, 6, 8, 'Разносторонний треугольник'],
    )
)
def test_zad_1_3(side1, side2, side3, answer):
    result = check_triangle(side1, side2, side3)
    assert result == answer
