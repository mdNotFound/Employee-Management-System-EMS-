#Planning a data storage system for an employee management application
# The data will be stored in a dictionary where each employee's ID is the key and the value is a dictionary containing their name, age, department, and salary
employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Aisha', 'age': 30, 'department': 'IT', 'salary': 60000}
}
#Defining the menu system
def main_menu():
    while True:
        print("\nWelcome to the Employee Management System")
        print("1. Add Employee")
        print("2. View all Employees")
        print("3. Search for Employee")
        print("4. Exit")

        choice = (input("Enter your choice (1-4): "))
        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print("Thank you for using the Employee Management System. Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")

def add_employee():
    emp_id = int(input("Enter employee ID: "))
    if emp_id in employees:
        print("Employee ID already exists. try again.")
        add_employee()
    else:
        name = input("Enter employee name: ")
        age = int(input("Enter employee age: "))
        department = input("Enter employee department: ")
        salary = int(input("Enter employee salary: "))
        employees[emp_id] = {'name': name, 'age': age, 'department': department, 'salary': salary}
        print("Employee was successfully added.")

def view_employees():
    if not employees:
        print("No employees available.")
    else:
        print("Employee ID\tEmployee Name\tEmployee Age\tEmployee Department\tEmployee Salary")
        for emp_id, employee in employees.items():
            print("{:<10} {:<15} {:<5} {:<15} {:<10}".format(emp_id, employee['name'], employee['age'], employee['department'], employee['salary']))
           
def search_employee():
    emp_id = int(input("Enter employee ID: "))
    if emp_id in employees:
        employee = employees[emp_id]
        print(f"Employee ID: {emp_id}")
        print(f"Employee Name: {employee['name']}")
        print(f"Employee Age: {employee['age']}")
        print(f"Employee Department: {employee['department']}")
        print(f"Employee Salary: {employee['salary']}")
    else:
        print("Employee not found.")

main_menu()