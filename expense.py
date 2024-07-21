import csv
import pandas as pd

def add_expense(filename, salary):
    while True:
        total_expense = []
        filename = "./users_expenses/" + filename
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                total_expense.append(row[1])
        total = 0
        for i in total_expense:
            total += int(i)
        remaining = int(salary) - total
        print(f"Your total expense is: {total}\nRemaining Expense is: {remaining}")
        filename = "./users_expenses/" + filename
        item = input("Enter item: ")
        price = input("Enter price: ")
        with open(filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([item, price])
        print("Expense added successfully")
        choi = input("Do you want to add more? (y/n): ")
        if choi == "y":
            continue
        else:
            break

def show_expense(filename, salary):
    total_expense = []
    filename = "./users_expenses/" + filename
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            total_expense.append(row[1])
    total = 0
    for i in total_expense:
        total += int(i)
    remaining = int(salary) - total
    print(f"Your total expense is: {total}\nRemaining Expense is: {remaining}")
    # filename = "./users_expenses/" + filename
    df = pd.read_csv(filename)
    print(df.to_string())
