from datetime import datetime

class FullTimeEmployee:
    def save(self, name, salary):
        try:
            with open("id.txt", "r") as id_file:
                content = id_file.read().strip()
                emp_id = int(content) if content else 1  # fallback to 1
        except FileNotFoundError:
            emp_id = 1 

        time_now = datetime.now().strftime("%B %d , %Y") #add current date

        with open("employee.txt", "a") as f:
            f.write(f"ID : {str(emp_id)}  |  Name: {name}  | Type: Full-Time  | Salary: {salary} | Date : {time_now} \n")
        
        with open("id.txt", "w") as id_file:
            id_file.write(str(emp_id + 1))

        print("Saved to file!\n")
        print("******************************************")


class PartTimeEmployee:
    def save(self, name, salary):
        try:
            with open("id.txt", "r") as id_file:
                content = id_file.read().strip()
                emp_id = int(content) if content else 1 
        except FileNotFoundError:
            emp_id = 1 

        time_now = datetime.now().strftime("%B %d , %Y")

        with open("employee.txt", "a") as f:
           f.write(f"ID : {str(emp_id)}  |  Name: {name}  | Type: part-Time  | Salary: {salary} | Date : {time_now} \n")
        
        with open("id.txt", "w") as id_file:
            id_file.write(str(emp_id + 1))

        print("Saved to file!\n")
        print("******************************************")


while True:
    print('''
Welcome to Employee Manager
1. Add Full-Time Employee
2. Add Part-Time Employee
3. Show All Employees
4. Search By Name
5. Exit
6. Clear All Records
7. Show Total Employee
''')

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter your name: ")
        salary = int(input("Full-Time salary: "))
        emp = FullTimeEmployee()
        emp.save(name, salary)

    elif choice == 2:
        name = input("Enter your name: ")
        salary = int(input("Part-Time salary: "))
        emp = PartTimeEmployee()
        emp.save(name, salary)

    elif choice == 3:
        try:
            with open("employee.txt", "r") as f:
                content = f.read()
                if content:
                    print("Employee Records:\n")
                    print(content)
                    print("******************************************")

                else:
                    print("No employee records found.\n")
        except FileNotFoundError:
            print("No employee file found yet.\n")

    elif choice == 4:
        search_name = input("Enter name to be Search : ").lower()
        with open("employee.txt","r") as f:
            found = False
            for line in f:
               if search_name in line.lower():
                   print("found : ",line.strip())
                   print("******************************************")

                   found = True
            if not found:
                print("No record found with this name .")

    elif choice == 5:
        print("Exiting Employee Manager. Have a nice day!\n")
        break  #  This exits the loop

    elif choice == 6:
        del_ch = input("Are you sure? (y/n) : ")
        if del_ch == "y":
            with open("employee.txt" , "w") as f:
                f.write("")
            with open("id.txt","w") as t:
                t.write("")
            print("******************************************")
        else:
            break
    
    elif choice == 7:
        with open("employee.txt" , "r") as f:
            line = f.readlines()
            print(f"\nTotal Employee : {len(line)}")
            print("******************************************")
    else:
        print("Invalid choice. Please select 1-4.\n")

