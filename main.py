import auth
import expense

def print_heading(str):
    print(f"------------------------------{str}------------------------------")
def main():
    print_heading("Welcome to Expense manager")
    print_heading("Please login to continue")
    username, password, salary = auth.login()
    file= username + ".csv"
    while True:
        print_heading("Select a choice, what you want to perform")
        print("1. Add expense")
        print("2. Show expense")
        print("3. Add income")
        print("4. Show income")
        print("5. Show report")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("Add expense")
            expense.add_expense(file)
        elif choice == "2":
            print("Show expense")
            expense.show_expense(file)
        elif choice == "3":
            print("Add income")
        elif choice == "4":
            print("Show income")
        elif choice == "5":
            print("Show report")
        elif choice == "6":
            print("Exit")
            break
        else:
            print("Invalid choice")
    print_heading("Thank you for using Expense manager")
    print_heading("Goodbye!")
    print(username)
    print(password)
    print(salary)
if __name__ == "__main__":
    main()