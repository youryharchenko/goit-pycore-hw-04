import pickle
import pathlib

from typing import Dict

def read_dict(path: pathlib.Path) -> Dict[str, str]:
    """ Заванатажує довідник з файла

    path -- шлях до довідника
    """
    if path.exists():
        try:
            with open(path, 'rb') as f:
                return pickle.load(f)
        except Exception as ex:
            print("Loading Contacts error: {ex}, creating new dictionary")
            return {}
    else:
        # Якщо довідника ще нема, то повертаємо поржній
        return {}
    
def write_dict(path: pathlib.Path, dict: Dict[str, str]):
    """ Записує довідник в файл

    path -- шлях до довідника
    dict -- словник довідника
    """
    with open(path, "wb") as f:
        pickle.dump(dict, f)

def main():
    script_path = pathlib.Path(__file__)
    dict_path = script_path.with_name('contacts.pickle')
    dict = read_dict(dict_path)

    # Handler: add name phone - додає новий контакт
    def add(name: str, phone: str):
        dict[name] = phone
        write_dict(dict_path, dict)
        print(f"Phone {phone} to {name} added")

    # Handler: change name phone - змінює існуючий контакт
    def change(name: str, phone: str):
        if name in dict:
            dict[name] = phone
            write_dict(dict_path, dict)
            print(f"Contact {name}: {phone} changed")
        else:
            print(f"Contact {name} not found")
        
    # Handler: all - виводить всі контакти
    def print_all():
        for name, phone in dict.items():
            print(f"{name}: {phone}") 

    # Handler: phone name - виводить вказаний контакт
    def print_phone(name: str):
        phone = dict.get(name, f"Contact {name} not found") 
        print(f"{name}: {phone}")   

    print("Welcome to the assistant bot!")
    while True:
        repl = input("Enter a command: ")
        match repl.split():
            case ['add', name, phone]:
                add(name, phone)
            case ['change', name, phone]:
                change(name, phone)
            case ['all']:
                print_all()
            case ['phone', name]:
                print_phone(name)
            case ['exit'] | ['quit'] | ['close']:
                print("Good bye!")
                break
            case ['hello']:
                print("How can I help you?")
            case _:
                print(f"in-correct command: {repl}")
    

if __name__ == "__main__":
    main()