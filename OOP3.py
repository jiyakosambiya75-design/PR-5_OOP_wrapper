p1=None
e1=None
m1=None
Persons=[]
Employees=[]
Managers=[]
class Person :
    def __init__(self , name , age):
        self.name = name
        self.age = age
        
    def display(self):
        print(f"Person created with name : {self.name} and age : {self.age}.")
    
    def details(self):
        
        print(f"""
            "Name" : {self.name}, 
            "Age" : {self.age}
        """)

class Employee(Person):
    def __init__(self,name,age,employee_id=None,salary=None):
        super().__init__(name,age)
    
        self.__employee_id = employee_id
        self.__salary = salary
    
    def get_employee_id(self):
        return self.__employee_id
        
    def set_employee_id(self,employee_id):
        if employee_id != self.__employee_id :
            self.__employee_id = employee_id
            print("Employee ID Added successfully!!!" )
        else:
            print("This Employee id is already exist")
            
    def get_salary(self):
        return self.__salary
        
    def set_salary(self,salary):
        if salary > 0 :
            self.__salary =salary
            print("salary Updated successfully!!!" )
        else:
            print("salary can not Update")
        
    def display(self):
        print(f"Employee created with name : {self.name} and age : {self.age},ID:{self.get_employee_id()} and salary : {self.get_salary()}.")
        
    def details(self):
    
        print(f"""
        "Name" : {self.name},
        "Age" : {self.age},
        "Manager_ID" : {self.__employee_id},
        "Salary" : {self.__salary}
        """)

    def __del__(self):
        print(f"Employee {self.get_employee_id()} resources freed.")

class Manager(Employee):
    def __init__(self,name,age,employee_id,salary,department):
        super().__init__(name,age,employee_id,salary)
        
        self.department = department
    
    def display(self):
        print(f"Manager created with name : {self.name} and age : {self.age},ID:{self.get_employee_id()} salary : {self.get_salary()}.and department:{self.department}")
      
    def details(self):

          print(f"""
        "Name" : {self.name},
        "Age" : {self.age},
        "Manager_ID" : {self.get_employee_id()},
        "Salary" : {self.get_salary()},
        "Department" : {self.department},
        """)

print("="*50)
print("       ----- Python OOP Project -----")
print("="*50)
while True:
    print("""
    Choose an operation:
    1. Create a Person
    2. Create an Employee
    3. Create a Manager
    4. Show Details
    5. Check subclass
    6. Exit """)
    choice=int(input("Enter your choice: "))

    if choice == 1:
      name=input("Enter a person Name: ")
      age=int(input("Enter your age: "))
      p1=Person(name,age )
      Persons.append(p1)
      p1.display()
      print("\n------------ Choose another operation --------------")

    elif choice == 2:
      name=input("Enter a Employee Name: ")
      age=int(input("Enter your age: "))
      employee_id=input("Enter Employee ID: ")
      if any(employee.get_employee_id() == employee_id for employee in Employees):
        print("This Employee ID already exists!")
      else:
        salary = float(input("Enter Salary: "))
        e1 = Employee(name, age, employee_id, salary)
        Employees.append(e1)
        e1.display()
        print("\n------------ Choose another operation --------------")
    elif choice == 3 :
      name=input("Enter a Manager Name: ")
      age=int(input("Enter your age: "))
      employee_id=input("Enter Manager_ID: ")
      if any(Manager.get_employee_id() == employee_id for Manager in Managers):
        print("This Manager ID already exists!")
      else:
        salary = float(input("Enter Salary: "))
        department= input("Enter department: ")
        m1 = Manager(name, age, employee_id, salary, department)
        Managers.append(m1)
        m1.display()
      
      print("\n------------ Choose another operation --------------")
    elif choice == 4:
        print("choose details to show: ")
        print("1. Person ")
        print("2. Employee ")
        print("3. Manager ")
        ch=int(input("Enter your choice: "))
        if ch == 1:
            if Persons:
                count=1
                
                for Person in Persons:
                    print(f"\nPerson {count} Details")
                    Person.details()
                    count += 1
        
            else:
               print("Person is not exist right now!!")
               
        elif ch == 2:
            if Employees:
                count=1
                for Employee in Employees:
                    print(f"\nEmployee {count} Details")
                    Employee.details()
                    count+=1
            else:
                print("Employee is not exist right now!!")
                
        elif ch == 3:
            if Managers:
                count=1
                for Manager in Managers:
                    print(f"\nManager {count} Details")
                    Manager.details()
                    count+=1
            else:
               print("Manager is not exist right now!!")
        else:
            print("Invalid choice")
        print("\n------------ Choose another operation --------------")
    
    elif choice == 5:
        print(f"""Check issubclass\n1.Employee is subclass of person\n2.Manager is subclass of employee
        """)
        ch=int(input("Enter your choice: "))
        if ch == 1:
            print(issubclass(Employee,Person))
        elif ch == 2:
            print(issubclass(Manager,Employee))
        else:
            print("Invalid choice")
            
    elif choice == 6:
        print("Exiting the system. All resources have been freed.")
        break
    
    else:
        print("Invalid choice")
            
        print("\n------------ Choose another operation------------")
