import pandas as pd
import csv
username = 'some_username'
password = 'some_password'
salary = 'some_salary'
file = username + ".csv"
def print_heading(str):
    print(f"------------------------------{str}------------------------------")

def search_user(username):
    password= None
    with open("users.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username:
                password =  row[1]
                salary = row[2]
                break
    return password, salary

def register(username):
    print(f"Hello {username},")
    password = input("Create your password: ").strip()
    salary = input("Enter your salary/income: ").strip()
    filename = username + ".csv"
    with open("users.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, password, salary])
        print("New user created successfully")
    with open(filename, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["item", "price"])

def login():
    while True:
        username = input("Enter your user name: ").strip()
        password, salary = search_user(username)
        if password == 'some_password':
            print("Your are a new user")
            register(username)
            continue
        else:
            passw = input("Enter your password: ")
            if passw == password:
                print(f"Hello {username}, You have successfully logged in!")
                break
            else:
                print("Incorrect Password")
                continue

def choice():
    print()
def main():
    print_heading("Welcome to Expense manager") 
    login()

    choice = choice(username)
    
if __name__ == "__main__":
    main()