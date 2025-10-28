student = list()

student.append(input("Enter name: "))     
student.append(int(input("Enter age: ")))    

faculty_number = (input("Enter faculty number (exactly 9 digits): "))
if len(faculty_number) != 9 or not faculty_number.isdigit():
    faculty_number = "invalid"

student.append(faculty_number) 

print("\nStudent Information:")
print(f"Name: {student[0]}")
print(f"Age: {student[1]}")
print(f"Faculty Number: {student[2]}")
