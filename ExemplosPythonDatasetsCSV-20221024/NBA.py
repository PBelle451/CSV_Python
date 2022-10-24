import csv

fieldnames = ['id', 'name', 'age', 'height', 'weight', 'gender']
rows = [
    [1, 'Pedro', 20, 1.76, 74,'male'],
    [2,'Jamal', 23, 1.98, 98, 'male'],
    [3,'Speed', 17, 1.72, 64, 'male'],
    [4, 'Alexa', 26, 1.68, 55, 'female'],
    [5, 'Eivor', 24, 1.85, 80, 'female'],
    [6, 'John', 46, 1.70, 101, 'male'],
    [7, 'Robert', 20, 1.70, 63, 'male'],
    [8, 'Eric', 26, 1.82, 70, 'male'],
    [9, 'Sigurd', 30, 2.03, 95, 'male'],
    [10, 'Darcy', 56, 1.63, 52, 'female'],
]

with open('names-create.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(fieldnames)
    writer.writerows(rows)