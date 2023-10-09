import sys


school = {}


class Student:

    def __init__(self, name):
        self.name = name
        self.classes = None

    def add_classes(self):
        class_name = input('Klasa, w której się uczysz: ')
        if class_name not in school:
            self.classes = SchoolClass(class_name)
            school[class_name] = self.classes
        school[class_name].students.append(self.name)

    def display(self):
        print(f'Uczeń nazywa się {self.name} i uczy się w klasie {self.classes}.')


class Teacher:

    def __init__(self, name):
        self.name = name
        self.subject = None
        self.classes = []

    def add_classes(self):
        self.subject = input('Przedmiot, którego uczysz: ')
        while True:
            classes = input('Klasa, w której uczysz: ')
            if not classes:
                return
            if classes not in school:
                new_class = SchoolClass(classes)
                school[classes] = new_class
            new_class = school[classes]
            self.classes.append(new_class)
            new_class.teachers.append(self.name)

    def display(self):
        print(f'Nauczyciel nazywa się {self.name} i uczy w klasie {self.classes}.')


class Tutor:

    def __init__(self, name):
        self.name = name
        self.classes = []

    def add_classes(self):
        while True:
            classes = input('Klasa, która prowadzisz: ')
            if not classes:
                return
            if classes not in school:
                new_class = SchoolClass(classes)
                school[classes] = new_class
            new_class = school[classes]
            self.classes.append(new_class)
            new_class.tutors.append(self.name)

    def display(self):
        print(f'Wyvhowawca nazywa się {self.name} i prowadzi klasy  {self.classes}.')


class SchoolClass:

    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []
        self.subjects = []
        self.tutors = []

    def display(self):
        print(f'W tej klasie uczy się {self.students}.\n'
              f'Nauczyciele: {self.teachers}. \n'
              f'Wychowawcy: {self.tutors}.')

av_actions = ['uczeń', 'nauczyciel', 'wychowawca', 'koniec']

while True:
    action = input(f'Podaj funkcję {av_actions}: ')
    if action not in av_actions:
        print("Błędny wybór")
        continue
    if action == 'koniec':
        print('koniec')
        break
    name = input('Podaj imię i nazwisko: ')
    if action == 'uczeń':
        person = Student(name)
    if action == 'nauczyciel':
        person = Teacher(name)
    if action == 'wychowawca':
        person = Tutor(name)
    person.add_classes()
    school[name] = person

if len(sys.argv) > 1:
    argv1 = sys.argv[1]
    print(f'Z wejścia pobrano: {argv1}')
    person = school.get(argv1)
    if person:
        person.display()
