from pathlib import Path

with open('file.txt', 'w',encoding= "UTF-8") as fh:
    fh.write("Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000")

def total_salary(path):
    total = 0 
    num = 0
    with open('file.txt','r',encoding= "UTF-8") as fh:
        for line in fh:
            name, salary_string = line.strip().split(",")
            salary = int(salary_string)
            total += salary
            num += 1
            if num == 0:
                return 0
            average = int(total / num)
    return total, average

total, average = total_salary("path/to/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")