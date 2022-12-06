"""
import csv
with open ("book2.csv", newline="") as csvfile:
    rows = csv.reader(csvfile, delimiter=",")
    data = []
    for row in rows:
        data.append(row)

for item in data:
    print(item[1])

pokemon = input("Enter the name of the Pokemon or its number")
"""
import csv
with open ("book2.csv", newline="") as csvfile:
    rows = csv.reader(csvfile, delimiter=",")
    data = []

def searchByNumber():
    number = input("Enter pokemon number\n")
    csv_file = csv.reader(open("book2.csv", "r"))

    for row in csv_file:
        if number == row[0]:
            print(row)


def searchByName():
    name = input("Enter pokemon name\n")
    csv_file = csv.reader(open("book2.csv", "r"))

    for row in csv_file:
        if name in row[1]:
            print(row)


print("Enter 1 to search by pokemon number")
print("Enter 2 to search by pokemon name")

src = int(input("Enter here: "))

if src == 1:
    searchByNumber()
elif src == 2:
    searchByName()
else:
    print("Invalid")
