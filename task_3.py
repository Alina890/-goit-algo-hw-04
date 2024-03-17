from pathlib import Path
import sys

def get_structure(directory):
    def get_recursivelly(folder,indent = ""):
        for item in folder.iterdir():
            if item.is_dir():
                print(indent + "📂" + item.name)
                get_recursivelly(item, indent + " ")
            else:
                print(indent + "📜" + item.name)
        print("📦" + str(directory))
    get_recursivelly(directory)
    return

current_directory = Path(sys.path[0])
print (get_structure(current_directory))



