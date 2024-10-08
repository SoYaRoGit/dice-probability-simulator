# dice-probability-simulator

## Введение

dice-probability-simulator — это симулятор бросков игральной кости, реализованный на Python с использованием библиотеки Pydantic для валидации данных и collections.Counter для подсчёта результатов. Программа позволяет пользователю задать количество бросков кубика и возвращает статистику по результатам бросков, например, сколько раз выпала каждая грань (от 1 до 6).

## Основные компоненты проекта
Pydantic для валидации данных: Используется для валидации введенного пользователем количества бросков кубика, ограничивая диапазон значений от 1 до 10 миллионов.

Игральная кость (Cube): Класс, который симулирует броски кубика и использует random.randint для генерации случайных значений от 1 до 6.

Подсчёт результатов: После каждого броска кубика результаты сортируются и подсчитываются с помощью Counter, предоставляя пользователю удобную сводку по каждому числу, выпавшему на кубике.

## Пример вывода:
```console
Введите количество подкидываний: 10
Количество 1 = 3
Количество 3 = 2
Количество 4 = 1
Количество 5 = 2
Количество 6 = 2
```

## Для чего этот проект

Это служит практикой для работы с основными концепциями Python:

Валидация данных с помощью Pydantic.
Работа с коллекциями и подсчётом элементов с использованием Counter.
Использование генераторов случайных чисел и реализация простых алгоритмов сортировки.

## Как использовать проект

Активируйте виртуальное окружение
```bash
poetry shell 
```

Установите библиотеки
```bash
poetry install
```

В случае, если проект не видит библиотеки явно укажите интерпретатор

-> Visual Studio Code
```bash
CTRL+SHIFT+P -> Select interpreter -> Poetry
```

Запустите main.py
```bash
python src\main.py
```
