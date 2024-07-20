import csv
import pandas as pd

def add_expense(filename):
    while True:
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

def show_expense(filename):
    df = pd.read_csv(filename)
    print(df.to_string())
