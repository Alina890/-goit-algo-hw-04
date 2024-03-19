from pathlib import Path
import sys
from colorama import Fore, Style

def get_structure(directory):
    def get_recursivelly(folder,indent = ""):
        for item in folder.iterdir():
            if item.is_dir():
                print(indent + Fore.RED +"📂" + item.name)
                get_recursivelly(item, indent + " ")
            else:
                print(indent + Fore.GREEN +"📜" + item.name)
    get_recursivelly(directory)
    return

if len(sys.argv) < 2:
    print("Введіть шлях до папки")
else:
    directory_path = Path(sys.argv[1])
    if directory_path.exists() and directory_path.is_dir():
        get_structure(directory_path)
    else:
        print("Папка з вказаним ім'ям не існує")

current_directory = Path(".")
print (get_structure(current_directory))



