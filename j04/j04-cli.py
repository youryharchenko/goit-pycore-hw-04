import typer
import pickle
import pathlib


script_path = pathlib.Path(__file__)
dict_path = script_path.with_name('contacts.pickle')
print(dict_path)

def read_dict(path):
    if path.exists():
        with open(path, 'rb') as f:
            return pickle.load(f)
    else:
        return {}
    
def write_dict(path, dict):
    with open(path, "wb") as f:
        pickle.dump(dict, f)

app = typer.Typer()

@app.command()
def add(name: str, phone: str):
    dict = read_dict(dict_path)
    dict[name] = phone
    write_dict(dict_path, dict)
    print(f"Phone {phone} to {name} added")

@app.command()
def all():
    dict = read_dict(dict_path)
    for name, phone in dict.items():
        print(f"{name}: {phone}")

@app.command()
def phone(name: str):
    dict = read_dict(dict_path)
    phone = dict.get(name, f"Contact {name} not found") 
    print(f"{name}: {phone}")

@app.command()
def change(name: str, phone: str):
    dict = read_dict(dict_path)
    old = dict.get(name)
    if old == None:
        print(f"Contact {name} not found")
    else:
        dict[name] = phone
        write_dict(dict_path, dict)
        print(f"Contact {name}: {phone} changed")


def main():
    app()


if __name__ == "__main__":
    main()