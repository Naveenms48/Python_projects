from abc import ABC,abstractmethod

class Person(ABC):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @abstractmethod
    def show_details(self):
        pass

class Student(Person):
    def __init__(self, name, age,student_id,grade):
        super().__init__(name, age)
        self.__student_id = student_id
        self.grade = grade

    def get_id(self):
        return self.__student_id

    def show_details(self):
        print(f"Name : {self.name}, Age : {self.age}, Student_ID : {self.__student_id}, Grade : {self.grade} ")

class Teacher(Person):
    def __init__(self, name, age,subject):
        super().__init__(name, age)
        self.subject = subject
    
    def show_details(self):
        print(f"Name : {self.name}, Age : {self.age}, Subject : {self.subject}")

class ManagementSystem:
    def __init__(self):
        self.people = []  

    def add_person(self,person):
        self.people.append(person)
        print(f"✅ {person.name} Added Successfully")

    def remove_student(self,student_id):
        for p in self.people:
            if isinstance(p,Student) and p.get_id() == student_id:
                self.people.remove(p)
                print(f"Student {p.name} removed Successfully")
                return
        print("⚠️ Student not found")

    def search_student(self,student_id):
        for p in self.people:
            if isinstance(p,Student) and p.get_id() == student_id:
                print("Student Found")
                p.show_details()
                return
        print(f"⚠️ Student not found")

    def display_all(self):
        if not self.people:
            print("⚠️ No records found")
        
        else:
            print("📌All Records")
            for p in self.people:
                p.show_details()

system = ManagementSystem()

while True:
    print("\n===== 📚 Student Management System =====")
    print("1. Add Student")
    print("2. Add Teacher")
    print("3. Remove Student")
    print("4. Search Student")
    print("5. Display All")
    print("6. Exit")

    choice = int(input("Enter your choice (1-6) : "))

    if choice == 1:
        try:
            name = input("Enter student name : ").strip()
            age = int(input("Enter student age : "))
            student_id = input("Enter student id : ").strip()
            grade = input("Enter student grade : ").strip()
            student = Student(name,age,student_id,grade)
            system.add_person(student)
        
        except (ValueError,TypeError) as e:
            print("Error",e)

    elif choice == 2:
        try:
            name = input("Enter teacher name : ").strip()
            age = int(input("Enter teacher age : "))
            subject = input("Enter subject name : ").strip()
            teacher = Teacher(name,age,subject)
            system.add_person(teacher)

        except (ValueError,TypeError) as e:
            print("Error",e)
    
    elif choice == 3:
        student_id = input("Enter student id to remove : ")
        system.remove_student(student_id)

    elif choice == 4:
        student_id = input("Enter student id to search : ")
        system.search_student(student_id)

    elif choice == 5:
        system.display_all()

    elif choice == 6:
        print("Thank You")
        print("👋Existing... Good Boy!")
        break

    else:
        print("⚠️Invalid Choice.Please Try Again")
