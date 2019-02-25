class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return "{}:{}".format(self.name, self.score)


students = [
    Student("김일수", 10),
    Student("김삼수", 30),
    Student("김이수", 20)
]

fss = filter(lambda stu: stu.score >= 20, students)
for fs in fss:
    print(fs)

print("=========================")

def print_students():
    print("--------------------")
    for s in students:
        print(s)


students = sorted(students, key=lambda stu: stu.score)
print_students()

students.sort(key=lambda stu: stu.score)
print_students()
