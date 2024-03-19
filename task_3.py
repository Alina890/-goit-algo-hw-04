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

current_directory = Path(".")
print (get_structure(current_directory))



