from pathlib import Path

with open('file_cat.txt', 'w',encoding= "UTF-8") as fh:
    fh.write("60b90c1c13067a15887e1ae1,Tayson,3\n60b90c2413067a15887e1ae2,Vika,1\n60b90c2e13067a15887e1ae3,Barsik,2\n60b90c3b13067a15887e1ae4,Simon,12\n60b90c4613067a15887e1ae5,Tessi,5")

def get_cats_info(path):
    cats_info = []
    with open('file_cat.txt','r',encoding= "UTF-8") as fh:
        for line in fh:
            cat_date = line.strip().split(",")
            cat_info = {"id": cat_date[0], "name": cat_date[1], "age": int(cat_date[2])}
            cats_info.append(cat_info)
    return cats_info
            
cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)