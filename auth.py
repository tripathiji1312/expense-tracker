import csv

def encryption(stri, file_path="auth.csv"):
    encrypted_string = ""
    for i in stri:
        with open(file_path, "r", newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if str(row[0]) == str(i):
                    encrypted_string += str(row[1])
                    break
    return encrypted_string

def decryption(stri, file_path="auth.csv"):
    decrypted_string = ""
    for i in stri:
        with open(file_path, "r", newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if str(row[1]) == str(i):
                    decrypted_string += str(row[0])
                    break
    return decrypted_string

def login():
    while True:
        username = input("Enter your user name: ").strip()
        password, salary = search_user(username)
        if not password:
            print("You are a new user")
            register(username)
            continue
        else:
            passw = input("Enter your password: ")
            if passw == decryption(password):
                print(f"Hello {username}, You have successfully logged in!")
                break
            else:
                print("Incorrect Password")
                continue
    return username, password, salary

def search_user(username):
    password = None
    salary = None
    with open("users.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username:
                password = row[1]
                salary = row[2]
                break
    return password, salary

def register(username):
    print(f"Hello {username},")
    password = input("Create your password: ").strip()
    encrypted_password = encryption(password)
    salary = input("Enter your salary/income: ").strip()
    filename = username + ".csv"
    with open("users.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, encrypted_password, salary])
        print("New user created successfully")
    with open(filename, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["item", "price"])

if __name__ == "__main__":
    login()
