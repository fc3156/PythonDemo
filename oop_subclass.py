# encoding=UTF-8

class SchoolMember:
    '''代表任何学校里的成员'''

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember:{})'.format(self.name))

    def tell(self):
        '''告诉我有关的细节'''
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")


class Teacher(SchoolMember):
    '''代表一位老师'''

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher:{})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary:"{}"'.format(self.salary))


class Student(SchoolMember):
    '''代表一位学生'''

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student:{})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))

#下面开始建立对象
t = Teacher('Mrs.linda', 40, 30000)
s = Student('Swaroop', 25, 90)

# 打印一个空白行
print()

members = [t, s]
for member in members:
    member.tell()
