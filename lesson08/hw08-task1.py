import csv
from prettytable import from_csv


def main():
    filename = "database.csv"
    header = ("id", "Название", "Автор", "Жанр", "Год издания", "Издательство", "Цена")
    data = [
        (0, "Дизайн для реального мира", "Виктор Папанек", "Наука и образование", "2017", "Д.Аронов", 400),
        (1, "Укус Питона", "Сваруп Читлор", "Наука и образование", "2017", "Интернет", 600)
    ]

    try:
        csvfile = open(filename)
    except IOError:
        print("Database file not found, created new file")
        writer(header, data, filename, "write")
    print_table(filename)

    print("1. Edit record.")
    print("2. Append record.")
    print("3. Exit.")
    print()
    option_num = int(input("Select option: "))
    if option_num == 1:
        option = "edit"
        id = int(input("Input record number: "))
        col = input("Input column name: ")
        val = input("Input record value: ")
        editor(filename, id, col, val)
    elif option_num == 2:
        print("Option is temporary unavailable")
    elif option_num == 3:
        exit()


def writer(header, data, filename, option):
    with open(filename, "w", newline="") as csvfile:
        if option == "write":
            records = csv.writer(csvfile, delimiter='*')
            records.writerow(header)
            for x in data:
                records.writerow(x)
        elif option == "edit":
            writer = csv.DictWriter(csvfile, fieldnames=header, delimiter='*')
            writer.writeheader()
            writer.writerows(data)
        else:
            print("Option is not known")


def editor(filename, id, col, val):
    with open(filename, newline="") as csvfile:
        readData = [row for row in csv.DictReader(csvfile, delimiter='*')]
        readData[id][col] = val
    readHeader = readData[0].keys()
    writer(readHeader, readData, filename, "edit")
    print_table(filename)

def print_table(filename):
    csvfile = open(filename, "r")
    table = from_csv(csvfile)
    csvfile.close()
    print(table)

if __name__ == "__main__":
    main()

