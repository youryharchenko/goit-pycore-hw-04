
from typing import Tuple

def total_salary(path: str) -> Tuple[float, float]:
    # Масив для зарплат
    salaries = []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            # Лічильник записів файлу
            i = 0
            # Цикл по записах
            for row in f.readlines():
                i += 1
                # Розбиваєимо запис на поля
                record = row.split(',')
                # Якщо кількість полів запису коректна, то обробляємо
                if len(record) == 2:
                    # Видалимо зайві пробіли
                    field = record[1].strip()
                    # Якщо поле містить число, то обробляємо
                    if field.isnumeric(): 
                        # Додаєио до масиву
                        salaries.append(float(field))
                    else:
                        # Інакше виводимо повідомлення
                        print(f"нечислове поле salary, запис #{i}: '{row}' ігнорується")    
                else:
                    # Інакше виводимо повідомлення
                    print(f"некоректний запис #{i}: '{row}' ігнорується")
    except FileNotFoundError:
        print(f"файл '{path}' не знайдено")
        return (0, 0)
    
    # Обчислюємо загальну суму
    suma = sum(salaries)
    # Обчислюємо середню ЗП
    mean = suma / len(salaries)
    # Повертаємо результат
    return (suma, mean)

    
    

import sys

if __name__ == "__main__":
    file_path = 'salary.txt'
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    print(file_path)
    result = total_salary(file_path)
    print(f"Загалом: {result[0]}, Середня: {result[1]}")