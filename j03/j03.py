import pathlib
from colorama import Fore, Style

def walk(pref: str, curr_path: pathlib.Path, result: str) -> str:
    """Обхід та побудова текстової структури директорії

    Аргументи:
    pref -- відступ рівня структури, 
    curr_path -- поточний елемент структури, 
    result -- рядок, де будується текстова структура
    """
    # Якщо файл, то просто додаємо рядок 
    if curr_path.is_file():
        result += f"{pref}{Fore.GREEN}{curr_path.name}{Style.RESET_ALL}\n"
    # Якщо директорія, то додаємо рядок та рекурсивно зпапускаємо її обхід
    elif curr_path.is_dir():
        result += f"{pref}{Fore.BLUE}{curr_path.name}/{Style.RESET_ALL}\n"
        for item in curr_path.iterdir():
            result = walk(pref + "  ", item, result)
    
    return result


def dir_tree(path: str) -> str:
    # Отримаємо об'єкт абсолютного шляху
    root_path = pathlib.Path(path).resolve()
    # Шлях має існувати і це має бути директорія
    if root_path.exists() and root_path.is_dir():
        # Викликаємо рекурсивну функцію обходу та побудови структури
        result = walk("", root_path, "")
    else:
        # Інакше повертаємо повідомлення
        result = f"{Fore.RED}'{path}' не існує або не директорія{Style.RESET_ALL}"
    return result

import sys

if __name__ == "__main__":
    path = '.'
    # Якщо є параметр візьмемо його, інакше буде поточна директорія
    if len(sys.argv) > 1:
        path = sys.argv[1]
    # Викликаєио функцію, яка побудує структуру як текст
    result = dir_tree(path)
    # Виведемо на консоль
    print(result)    