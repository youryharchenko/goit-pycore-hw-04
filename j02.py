from typing import List, Dict

def get_cats_info(path: str) -> List[Dict]:
    # Масив для зарплат
    cats: List[Dict] = []
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
                if len(record) == 3:
                    # Видалимо зайві пробіли
                    id = record[0].strip()
                    name = record[1].strip()
                    age = record[2].strip()
                    # Якщо поле 'age' містить число, то обробляємо
                    if age.isnumeric(): 
                        # Додаєио словник до масиву
                        cats.append({'id': id, 'name': name, "age": float(age)})
                    else:
                        # Інакше виводимо повідомлення
                        print(f"нечислове поле 'age', запис #{i}: '{row}' ігнорується")    
                else:
                    # Інакше виводимо повідомлення
                    print(f"некоректний запис #{i}: '{row}' ігнорується")
    except FileNotFoundError:
        print(f"файл '{path}' не знайдено")
        return []
        
    # Повертаємо результат
    return cats
   

import sys

if __name__ == "__main__":
    file_path = 'cats.txt'
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    print(file_path)
    result = get_cats_info(file_path)
    print(f"Котики:\n{result}")    