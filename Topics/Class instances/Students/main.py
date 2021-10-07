class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = str(birth_year)
        self.student_id = self.name[0] + self.last_name + self.birth_year

first_name_input = input()
last_name_input = input()
birth_year_input = input()


student = Student(first_name_input, last_name_input, birth_year_input)

print(student.student_id)



