import pathlib
from colorama import Fore, Style

def walk(pref: str, curr_path: pathlib.Path, result: str) -> str:
    if curr_path.is_file():
        result += f"{pref}{Fore.GREEN}{curr_path.name}{Style.RESET_ALL}\n"
    elif curr_path.is_dir():
        result += f"{pref}{Fore.BLUE}{curr_path.name}/{Style.RESET_ALL}\n"
        for item in curr_path.iterdir():
            result = walk(pref + "  ", item, result)
    
    return result


def dir_info(path) -> str:
    root_path = pathlib.Path(path).resolve()
    result = walk("", root_path, "")
    return result

import sys

if __name__ == "__main__":
    path = '..'
    if len(sys.argv) > 1:
        path = sys.argv[1]
    #print(dir_path)
    result = dir_info(path)
    print(result)    