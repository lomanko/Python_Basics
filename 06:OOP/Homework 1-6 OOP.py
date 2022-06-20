class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    # метод для оценки лекций у класса Lecturer
    def rate_lecture(self, lecturer, course, grade):
        # проверка, что lecturer является объектом соответствующего класса;
        # проверка, что оценка от 0 до 10 баллов;
        # проверка, что курс есть в courses_attached у лектора;
        # проверка, что курс есть в courses_in_progress у студента.
        if isinstance(lecturer, Lecturer) and 0 <= grade <= 10 and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.lecture_marks:
                lecturer.lecture_marks[course] += [grade]
            else:
                lecturer.lecture_marks[course] = [grade]
        else:
            return 'Ошибка'
    
    def average_hw_grades(self):
        res = sum(sum(self.grades.values(),[])) #сумма оценок
        quantity = len(sum(self.grades.values(),[])) #количество оценок
        if quantity > 0:
            return (res / quantity)
        else:
            return 'Оценок нет'
        
    def __str__(self):
        res = f'''
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за ДЗ: {self.average_hw_grades()}
        Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
        Завершенные курсы: {', '.join(self.finished_courses)}
        '''
        return res
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Некорректное сравнение.')
            return
        if self.average_hw_grades() == 'Оценок нет' or other.average_hw_grades() == 'Оценок нет':
            return 'Сравнение невозможно, т.к. у одного из студентов нет оценок'
        return self.average_hw_grades() < other.average_hw_grades()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecture_marks = {}
    
    def average_lecture_marks(self):
        res = sum(sum(self.lecture_marks.values(),[])) #сумма оценок
        quantity = len(sum(self.lecture_marks.values(),[])) #количество оценок
        if quantity > 0:
            return (res / quantity)
        else:
            return 'Оценок нет'
    
    def __str__(self):
        #res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_lecture_marks()}'
        res = f'''
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за лекции: {self.average_lecture_marks()}
        '''
        return res
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Некорректное сравнение.')
            return
        if self.average_lecture_marks() == 'Оценок нет' or other.average_lecture_marks() == 'Оценок нет':
            return 'Сравнение невозможно, т.к. у одного из лекторов нет оценок'
        return self.average_lecture_marks() < other.average_lecture_marks()

class Reviewer(Mentor):
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Перезагрузка метода str для проверяющего
    def __str__(self):
        res = f'''
        Имя: {self.name}
        Фамилия: {self.surname}
        '''
        return res

# Создадим по экземпляры классов Student, Lecturer, Reviewer
some_student = Student('Ivan', 'Ivanov', 'male')
second_student = Student('Svetlana', 'Mironova', 'female')
another_student = Student('Olga', 'Petrova', 'female')

some_lecturer = Lecturer('Sergey', 'Sergeev')
second_lecturer = Lecturer('Petr', 'Petrov')
another_lecturer = Lecturer('Oleg', 'Sidorov')

some_reviewer = Reviewer('Aleksandr', 'Petrov')
another_reviewer = Reviewer('Alekey', 'Popov')

# Добавим курсы студентам, лекторам и проверяющим
some_lecturer.courses_attached += ['Python','Java','HTML']
second_lecturer.courses_attached += ['Python','Java','Swift']
another_lecturer.courses_attached += ['C++','Java','Swift']

some_student.courses_in_progress += ['Python']
some_student.finished_courses += ['C++', 'Swift','Java']
another_student.courses_in_progress += ['Java', 'HTML']
second_student.courses_in_progress += ['Swift']

some_reviewer.courses_attached += ['Swift', 'HTML', 'Java']
another_reviewer.courses_attached += ['Java']

# Проверим метод оценки лекторов у студентов
some_student.rate_lecture(some_lecturer,'Python', 8)
some_student.rate_lecture(second_lecturer,'Python', 2)
another_student.rate_lecture(some_lecturer,'Java', 10)

# Проверим метод оценки дз у проверяющих
some_reviewer.rate_hw(another_student,'Java', 10)
some_reviewer.rate_hw(second_student,'Swift', 2)
another_reviewer.rate_hw(another_student,'Java', 6)

# Проверка перезагрузки метода __str__
print('Метод __str__ для класса Reviewer:')
print(some_reviewer)

print('Метод __str__ для класса Lecturer:')
print(another_lecturer) #случай, когда у лектора нет оценок
print(second_lecturer)

print('Метод __str__ для класса Student:')
print(some_student) #случай, когда у лектора нет оценок
print(second_student)

# Проверка перезагрузки метода __lt__

print('Метод __lt__ для класса Student:\n')
print(some_student < another_student) #случай, когда у одного из студентов нет оценок
print(second_student < another_student)

print('\nМетод __lt__ для класса Lecturer:\n')
print(some_lecturer < another_lecturer) #случай, когда у одного из студентов нет оценок
print(second_lecturer < some_lecturer)

print()

def average_course_student_grade(students, course_name):
    '''
    Функция принимает на вход список студентов (класс Student) и название курса.
    В результате средний бал по курсу среди списка студентов.
    '''
    average_mark = []
    for student in students:
        if isinstance(student, Student): #проверка на экземпляр класса
            if student.grades.get(course_name) != None: #проверка, что у студента есть оценки по курсу
                average_mark += student.grades.get(course_name)
        else:
            print('Некорректный список студентов.')
            return
    if len(average_mark) > 0: #проверка, что получился не пустой список оценок
        return sum(average_mark) / len(average_mark)
    else:
        return 'Оценок по данному курсу нет'
    
students = [some_student, second_student, another_student]
course_name = 'Java'

print(average_course_student_grade(students, course_name))

print() 

def average_course_lecturer_grade(lecturers, course_name):
    '''
    Функция принимает на вход список лекторов (класс Lecturer) и название курса.
    В результате средний бал по курсу среди списка лекторов.
    '''
    average_mark = []
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer): #проверка на экземпляр класса
            if lecturer.lecture_marks.get(course_name) != None: #проверка, что у студента есть оценки по курсу
                average_mark += lecturer.lecture_marks.get(course_name)
        else:
            print('Некорректный список преподователей.')
            return
    if len(average_mark) > 0: #проверка, что получился не пустой список оценок
        return sum(average_mark) / len(average_mark)
    else:
        return 'Оценок по данному курсу нет'
    
lecturers = [some_lecturer, second_lecturer, another_lecturer]
course_name = 'Python'

print(average_course_lecturer_grade(lecturers, course_name))