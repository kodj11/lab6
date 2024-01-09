class Student:
    
    def __init__(self, last_name, first_name, middle_name, group, grades):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.group = group
        self.grades = grades
        
    def __lt__(self, other):
        return self.get_avg_grade() < other.get_avg_grade()
    
    def __gt__(self, other):
        return self.get_avg_grade() > other.get_avg_grade()
        
    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name} {self.group} {self.grades[0]} {self.grades[1]} {self.grades[2]}"
    
    def get_avg_grade(self):
        return sum(self.grades) / len(self.grades)

    
def sort_by_grades(students):
    return sorted(students, key=lambda s: sum(s.grades)/len(s.grades), reverse=True)
    
NUM_STUDENTS = 5
students = []


with open('students.txt', 'r') as f:
    for i in range(NUM_STUDENTS):
        line = f.readline()
        parts = line.split() 
        students.append(Student(parts[0], parts[1], parts[2], int(parts[3]), 
                        [int(x) for x in parts[4:]]))


students = sort_by_grades(students)

# запись отсортированных данных в файл
with open('sorted_students.txt', 'w') as f:
    for s in students:
        f.write(str(s) + '\n')
        
print(f"Student: {students[0]} > student: {students[1]}? -> {students[0] > students[1]}")
