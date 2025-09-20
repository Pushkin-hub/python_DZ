grades = {"Иван": 5, "Мария": 4, "Пётр": 3}

name = input("Введите имя студента: ")

if name in grades:
    print(f"Оценка студента {name}: {grades[name]}")
else:
    print("Студент не найден")