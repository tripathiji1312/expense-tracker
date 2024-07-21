import csv

def update_salary(username, new_salary, file_path="users.csv"):
    rows = []
    index = ''
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            rows.append(row)
            if row[0] == username:
                index = i
    rows[index][2] = new_salary

    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
        print("Income updated successfully")

# update_salary("tripathiji", "50000")