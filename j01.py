
def total_salary(path: str):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            # Масив для зарплат
            salaries = []
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
            # Обчислюємо загальну суму
            suma = sum(salaries)
            # Обчислюємо середню ЗП
            mean = suma / len(salaries)
            # Повертаємо результат
            return (suma, mean)

    except FileNotFoundError:
        print(f"файл '{path} не знайдено")
    



if __name__ == "__main__":
    file_path = 'salary.txt'
    print(file_path)
    print(total_salary(file_path))