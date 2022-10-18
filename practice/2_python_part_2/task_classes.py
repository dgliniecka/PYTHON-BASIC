"""
Create 3 classes with interconnection between them (Student, Teacher,
Homework)
Use datetime module for working with date/time
1. Homework takes 2 attributes for __init__: tasks text and number of days to complete
Attributes:
    text - task text
    deadline - datetime.timedelta object with date until task should be completed
    created - datetime.datetime object when the task was created
Methods:
    is_active - check if task already closed
2. Student
Attributes:
    last_name
    first_name
Methods:
    do_homework - request Homework object and returns it,
    if Homework is expired, prints 'You are late' and returns None
3. Teacher
Attributes:
     last_name
     first_name
Methods:
    create_homework - request task text and number of days to complete, returns Homework object
    Note that this method doesn't need object itself
PEP8 comply strictly.
"""
import datetime as dt
class Teacher:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
    def create_homework(self, text, nod):
        return Homework(text, nod)
class Student:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
    def do_homework(self, homework):
        if homework.is_active() == True:
            print(student.first_name, 'does homework:')
            print('Homework is: ', homework.text, 'in', homework.number_of_days, 'days')
            return homework
        else:
            print('You are late')
class Homework:
    def __init__(self, text, nod):
        self.text = text
        self.number_of_days = nod
        self.created = dt.datetime.now()
        self.deadline = self.created + \
                        dt.timedelta(days = self.number_of_days)
    def is_active(self):
        if self.deadline >= dt.datetime.now():
            return True
        else:
            return False
if __name__ == '__main__':
    teacher = Teacher('Anna', 'Kowalska')
    t2 = Teacher('Piotr', 'Kowalski')
    student = Student('Diana', 'Gliniecka')
    expired_homework = teacher.create_homework('Learn functions', 0)
    super_homework = t2.create_homework('Paint', 2)
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too('create 2 simple classes', 5)
    student.do_homework(oop_homework)
    student.do_homework(expired_homework)
    student.do_homework(super_homework)