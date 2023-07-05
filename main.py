class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_st(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


    def grade_s(self):
        summ=[]
        for i in self.grades.values():
            summ += i
            x = round(sum(summ)/len(summ),1)
        return x

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции:{self.grade_s()} \nКурсы в процессе изучения: {', '.join(self.courses_in_progress)} \nЗавершенные курсы:{', '.join(self.finished_courses)}"

    def __lt__(self, other):
        print('Сравнение Студентов')
        if not isinstance(other, Student):
            print('Такое сравнение не корректно')
            return
        return  self.grade_s() < other.grade_s()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


    def grade_l(self):
        summ=[]
        for i in self.grades.values():
            summ += i
            x = round(sum(summ)/len(summ),1)
        return x

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции:{self.grade_l()}"

    def __lt__(self, other):
        print('Сравнение Лекторов')
        if not isinstance(other, Lecturer):
            print('Такое сравнение не корректно')
            return
        return  self.grade_l() < other.grade_l()

    def q(self, other):
        return self.grade(), other.grade()




class Rewiewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}"



# Добавляем студентов
best_student = Student('Иван', 'Иванов', 'муж')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']

best_student2 = Student('Антон', 'Сидоров', 'муж')
best_student2.courses_in_progress += ['Python', 'Git']
best_student2.finished_courses += ['Введение в программирование']


# Добавляем экспертов
cool_mentor = Rewiewer('Анна', 'Аннова')
cool_mentor.courses_attached += ['Python']
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 9)

cool_mentor = Rewiewer('Анна', 'Аннова')
cool_mentor.courses_attached += ['Git']
cool_mentor.rate_hw(best_student, 'Git', 7)
cool_mentor.rate_hw(best_student, 'Git', 7)
cool_mentor.rate_hw(best_student, 'Git', 9)

cool_mentor2 = Rewiewer('Дмитрий', 'Дмитриевич')
cool_mentor2.courses_attached += ['Python']
cool_mentor2.rate_hw(best_student2, 'Python', 9)
cool_mentor2.rate_hw(best_student2, 'Python', 10)
cool_mentor2.rate_hw(best_student2, 'Python', 10)

# Добавляем лекторов
cool_lec = Lecturer('Ольга', 'Олеговна')
cool_lec.courses_attached += ['Python']
best_student.rate_st(cool_lec, 'Python', 10)
best_student.rate_st(cool_lec, 'Python', 8)
best_student.rate_st(cool_lec, 'Python', 9)

cool_lec2 = Lecturer('Мария', 'Андреевна')
cool_lec2.courses_attached += ['Python']
best_student2.rate_st(cool_lec2, 'Python', 10)
best_student2.rate_st(cool_lec2, 'Python', 9)
best_student2.rate_st(cool_lec2, 'Python', 9)


print(cool_mentor)
print()
print(cool_mentor2)
print()

print(cool_lec)
print()
print(cool_lec2)
print()

# Сравнение студентов
print(f'Результат сравнения студентов(по средним оценкам за ДЗ): '
      f'{best_student.name} {best_student.surname} < {best_student2.name} {best_student2.surname} = {best_student > best_student}')
print()
# Сравнение лекторов
print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{cool_lec.name} {cool_lec.surname} < {cool_lec2.name} {cool_lec2.surname} = {cool_lec > cool_lec2}')
print()

students = [best_student, best_student2]
def student_rating(student, course_name):
    sum_all = []
    for stud in student:
        if course_name in stud.grades.keys():
            sum_all += stud.grades.get(course_name)
            x = round(sum(sum_all) / len(sum_all), 1)
    return x

print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(students, 'Python')}")

lecturers = [cool_lec, cool_lec2]
def lec_rating(lecturer, course_name):
    sum_all = []
    for lec in lecturer:
        if course_name in lec.grades.keys():
            sum_all += lec.grades.get(course_name)
            x = round(sum(sum_all) / len(sum_all), 1)
    return x

print(f"Средняя оценка для всех студентов по курсу {'Python'}: {lec_rating(lecturers, 'Python')}")