import auth
import expense
import income

def print_heading(str):
    print(f"------------------------------{str}------------------------------")
def main():
    print_heading("Welcome to Expense manager")
    print_heading("Please login to continue")
    username, password, salary = auth.login()
    file= username + ".csv"
    # file = "./users_expenses/" + file
    while True:
        print_heading("Select a choice, what you want to perform")
        print("1. Add expense")
        print("2. Show expense")
        print("3. Update income")
        print("4. Show income")
        print("5. Show report")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            print_heading("Add expense")
            expense.add_expense(file, salary)
        elif choice == "2":
            print_heading("Show expense")
            expense.show_expense(file, salary)
        elif choice == "3":
            print_heading("Update income")
            salary = input("Add new income: ")
            income.update_salary(username, salary)
        elif choice == "4":
            print_heading("Show income")
            print(f"Your salary is {salary}")
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