#!/usr/bin/env python3


# CONSTs, do not modify this part
NB_SUBJECTS = 3 # number of subjects we consider in the database
                # the default value is 3 which represents Chinese, Math and English
MAX_NUMBER = 999999 # maximum teacher job number allowed 
MAX_ID = 999999 # maximum student id number allowed


class Person(object):
    """
        superclass for Teacher and Student
        string name: fullname of the person, ex. "Zhang_San"
        bool gender: True stands for male and False stands for female
    """
    
    def __init__(self, _name, _gender):
        
        # datatype check
        assert type(_name) is str, \
            "Initialization Error, name of a person should be of type String. "
        assert type(_gender) is bool, \
            "Initialization Error, gender of a person should be of type Boolean. "
        
        # constructor 
        self.name = _name
        self.gender = _gender


class Teacher(Person):
    """
        class for teachers in Database, a subclass of Person
        int subject: code of the subject the teacher teaches, from 1 to NB_SUBJECTS
        int number: job number of the teacher, from 1 to MAX_NUMBER
    """
    
    def __init__(self, _name, _gender, _subject, _number):
        
        # superclass constructor
        super().__init__(_name, _gender)
        
        # datatype check 
        assert type(_subject) is int and 1 <= _subject and _subject <= NB_SUBJECTS, \
            f"Initialization Error, subject should be an Integer between 1 and {NB_SUBJECTS}. "
        assert type(_number) is int and 1<= _number and _number <= MAX_NUMBER, \
            f"Initialization Error, job number should be an Integer between 1 and {MAX_NUMBER}. "
        
        # constructor
        self.subject = _subject
        self.number = _number


class Student(Person):
    """
        class for students in Database, a subclass of Person
        int id: id number of the student
        Teacher teacher: teacher selected by the student, the default value is None
    """
    
    def __init__(self, _name, _gender, _id):
        
        # superclass constructor
        super().__init__(_name, _gender)
        
        # datatype check 
        assert type(_id) is int and 1 <= _id and _id <= MAX_ID, \
            f"Initialization Error, student id should be an Integer between 1 and {MAX_ID}. "
        
        # constructor
        self.id = _id
        self.teacher = None


class Database(object):
    """
        class for the after-school class database to manage teachers and students
        list teachers: teachers in the database, empty by default
        list students: students in the database, empty by default
    """
    
    # constructor
    def __init__(self):

        self.teachers = []
        self.students = []

    # a) return number of teachers
    def nb_teachers(self):
        
        return len(self.teachers)
    
    # b) return number of students
    def nb_students(self):
        
        return len(self.students)
    
    # c) return index of one teacher in teachers list by given job number
    def teacher_index_by_number(self, _number):
        
        for i in range(self.nb_teachers()):
            if self.teachers[i].number == _number:
                return i
        return -1
    
    # d) return index of one student in students list by given student id
    def student_index_by_id(self, _id):
        
        for i in range(self.nb_students()):
            if self.students[i].id == _id:
                return i
        return -1

    # e) add one teacher into the database
    def add_teacher(self, _name, _gender, _subject, _number):
        
        # verify if this teacher is already in the database
        if self.teacher_index_by_number(_number) >= 0:
            print(f"Teacher {_number} is already in the database. ")
        
        else:
            self.teachers.append(Teacher(_name, _gender, _subject, _number))
    
    # f) add one student into the database
    def add_student(self, _name, _gender, _id):
        
        # verify if this student is already in the database
        if self.student_index_by_id(_id) >= 0:
            print(f"Student {_id} is already in the database. ")
        
        else:
            self.students.append(Student(_name, _gender, _id))

    # g) return student / teacher ratio
    def ratio(self):
        
        # dev/0 check
        if self.nb_teachers() == 0:
            print("No teacher in the database, ratio not available. ")
            return None
        
        else:
            return self.nb_students() / self.nb_teachers()

    # h) print list of teachers of a subject and return number of the teachers
    def teachers_of_subject(self, _subject):
        
        # int count to count number of teachers of this subject
        count = 0
        output = ""
        
        for teacher in self.teachers:
            if teacher.subject == _subject:
                count += 1
                output += f"{teacher.name} "
        
        # verify if this subject has at least one teacher
        if count == 0:
            print(f"Subject of code {_subject} has no teacher. ")
        
        else:
            print(f"Subject of code {_subject} has {count} teacher(s):", output)
        
        return count

    # i) let one student of given id select one teacher by given teacher job number
    def select_teacher(self, _id, _number):
        
        # verify if student and teacher are both in the database
        student_index = self.student_index_by_id(_id)
        teacher_index = self.teacher_index_by_number(_number)
        if student_index < 0:
            print(f"Student of id {_id} not found in the database. ")
        elif teacher_index < 0:
            print(f"Teacher of job number {_number} not found in the database. ")
        
        # modify data of the student
        else:
            self.students[student_index].teacher = self.teachers[teacher_index]

    # j) print list of students of one teacher by given job number and return number of the students
    def students_of_teacher(self, _number):
        
        # verify if teacher is in the database
        teacher_index = self.teacher_index_by_number(_number)
        if teacher_index < 0:
            print(f"Teacher of job number {_number} not found in the database. ")
            return -1
            
        else:
            
            # int count to count number of teachers of this subject
            count = 0
            output = ""
            
            for student in self.students:
                if student.teacher == self.teachers[teacher_index]:
                    count += 1
                    output += f"{student.name} "
                    
            # verify if this teacher has at least one student
            if count == 0:
                print(f"Teacher of job number {_number} has no student. ")
            
            else:
                print(f"Teacher of job number {_number} has {count} student(s):", output)
                
            return count

    # k) return index of the teacher of one student by given id
    def teacher_of_student(self, _id):
        
        # verify if student is in the database
        student_index = self.student_index_by_id(_id)
        if student_index < 0:
            print(f"Student of id {_id} not found in the database. ")
            return -1

        # verify if student has chosen the teacher
        if self.students[student_index].teacher == None:
            print(f"Student of id {_id} hasn't choose any teacher. ")
            return -1
        
        # find the teacher index
        else:
            teacher_index = self.teacher_index_by_number(self.students[student_index].teacher.number)

            # verify if this teacher is in the database
            if teacher_index < 0:
                print(f"Student {_id} has chosen teacher {self.students[student_index].teacher.number} \
                        but the teacher is not in the database. ")
                return -1

            else:
                print(f"Student {_id} has chosen teacher {self.students[student_index].teacher.number}. ")
                return teacher_index

    # l) print list of students of one subject and return number of the students
    def students_of_subject(self, _subject):
        
        # int count to count number of students of this subject
        count = 0
        output = ""

        for student in self.students:
            if student.teacher is not None and student.teacher.subject == _subject:
                count += 1
                output += f"{student.name} "
        
        # verify if this subject has at least one student
        if count == 0:
            print(f"Subject of code {_subject} has no student. ")
        
        else:
            print(f"Subject of code {_subject} has {count} student(s):", output)
        
        return count

    # m) find most popular teacher in database and return the maximum number of students of that teacher
    def popular_teacher(self):
        
        # verify if database has at least one teacher
        if self.nb_teachers() == 0:
            print("No teacher in the database, most popular teacher not available. ")
            return 0
        
        # list max_list to store temporarily most popular teachers' index
        # int max_nb to store current number of students of most popular teacher
        max_list = [0]
        max_nb = self.students_of_teacher(self.teachers[0].number)
        output = f"{self.teachers[0].name} "

        # search for maximum
        for i in range(1, self.nb_teachers()):
            cur_nb = self.students_of_teacher(self.teachers[i].number)
            
            # more popular teacher found
            if cur_nb > max_nb:
                max_list = [i]
                max_nb = cur_nb
                output = f"{self.teachers[i].name} "
            
            # equaly popular teacher found
            elif cur_nb == max_nb:
                max_list.append(i)
                output += f"{self.teachers[i].name} "

        # verify if at least one teacher has at least one student
        if max_nb == 0:
            print("All teachers in the database have no corresponding student, most popular teacher not available. ")
            return 0

        else:
            print("Most popular teacher(s) is:", output)
            return max_nb

    # n) find most popular subject and return the maximum number of students of that subject
    def popular_subject(self):
        
        # verify if database allows at least one subject
        if NB_SUBJECTS < 1:
            print("No subject allowed in the database, most popular subject not available. ")
            return 0

        # list max_list to store temporarily most popular subjects
        # int max_nb to store current number of students of most popular subject
        max_list = [1]
        max_nb = self.students_of_subject(1)

        # search for maximum
        for i in range(2, NB_SUBJECTS + 1):
            cur_nb = self.students_of_subject(i)
            
            # more popular subject found
            if cur_nb > max_nb:
                max_list = [i]
                max_nb = cur_nb
            
            # equaly popular teacher found
            elif cur_nb == max_nb:
                max_list.append(i)

        # verify if at least one subject has at least one student
        if max_nb == 0:
            print("All subjects in the database have no corresponding student, most popular subject not available. ")
            return 0

        else:
            print("Code(s) of most popular subject(s) is:", max_list)
            return max_nb

    # o) print list of teachers with no student and return number of teachers
    def unselected_teachers(self):

        # int count to count number of teachers with no student
        count = 0
        output = ""

        for teacher in self.teachers:
            if self.students_of_teacher(teacher.number) == 0:
                count += 1
                output += f"{teacher.name} "

        # verify if at least one teacher has no student
        if count == 0:
            print(f"All teachers in the database has at least one student. ")

        else:
            print(f"{count} teacher(s) have no students:", output)

        return count

    # p) print list of students with no teacher and return number of the students
    def unselected_students(self):
        
        # int count to count number of students with no teacher
        count = 0
        output = ""

        for student in self.students:
            if student.teacher is None:
                count += 1
                output += f"{student.name} "
        
        # verify if at least one student has no teacher
        if count == 0:
            print(f"All students in the database has chosen teacher. ")

        else:
            print(f"{count} student(s) hasn't choose teacher:", output)

        return count

    # q) delete one student of given id from database
    def delete_student(self, _id):

        # verify if this student is in the database
        student_index = self.student_index_by_id(_id)
        if student_index < 0:
            print(f"Student of id {_id} is not in the database. ")

        else:
            del self.students[student_index]
            print(f"Student of id {_id} is removed from the database. ")

    # r) delete one teacher of given number from database
    def delete_teacher(self, _number):

        # verify if this teacher is in the database
        teacher_index = self.teacher_index_by_number(_number)
        if teacher_index < 0:
            print(f"Teacher of job number {_number} is not in the database. ")

        else:
            
            # change students' status who choose this teacher
            for student in self.students:
                if student.teacher == self.teachers[teacher_index]:
                    student.teacher = None
            
            del self.teachers[teacher_index]
            print(f"Teacher of job number {_number} is removed from the database. ")


# test functionalities of the database, do not modify this part and any function name above
def test():

    # __init__
    database = Database()
    assert database.nb_teachers() == 0, \
        "nb_teachers() incorrect"
    assert database.nb_students() == 0, \
        "nb_teachers() incorrect"

    # add_teacher
    database.add_teacher("teacher1-1", True, 1, 990101)
    database.add_teacher("teacher1-2", False, 1, 990102)
    database.add_teacher("teacher2-1", False, 2, 990201)
    database.add_teacher("teacher2-2", False, 2, 990202)
    assert database.nb_teachers() == 4, \
        "add_teacher() incorrect"
    database.add_teacher("teacher2-2", False, 2, 990202)
    assert database.nb_teachers() == 4, \
        "add_teacher() didn't consider whether the teacher is already in the database"

    # add_student
    database.add_student("student1", False, 100001)
    database.add_student("student2", True, 100002)
    database.add_student("student3", True, 100003)
    database.add_student("student4", False, 100004)
    database.add_student("student5", True, 100005)
    assert database.nb_students() == 5, \
        "add_student() incorrect"
    assert database.students[0].teacher is None \
        and database.students[1].teacher is None \
        and database.students[2].teacher is None \
        and database.students[3].teacher is None \
        and database.students[4].teacher is None, \
            "__init__ didn't initialize Student.teacher properly"
    database.add_student("student5", True, 100005)
    assert database.nb_students() == 5, \
        "add_student() didn't consider whether the student is already in the database"
    
    # teacher_index_by_number
    assert database.teacher_index_by_number(990101) == 0 \
        and database.teacher_index_by_number(990102) == 1 \
        and database.teacher_index_by_number(990201) == 2 \
        and database.teacher_index_by_number(990202) == 3, \
            "teacher_index_by_number() incorrect"
    assert database.teacher_index_by_number(990301) == -1, \
            "teacher_index_by_number() didn't consider whether the teacher is not in the database"

    # student_index_by_id
    assert database.student_index_by_id(100001) == 0 \
        and database.student_index_by_id(100002) == 1 \
        and database.student_index_by_id(100003) == 2 \
        and database.student_index_by_id(100004) == 3 \
        and database.student_index_by_id(100005) == 4, \
            "student_index_by_id() incorrect"
    assert database.student_index_by_id(100006) == -1, \
            "student_index_by_id() didn't consider whether the student is not in the database"

    # ratio
    assert database.ratio() == 1.25, \
        "ratio() incorrect"

    # teachers_of_subject
    assert database.teachers_of_subject(1) == 2 \
        and database.teachers_of_subject(2) == 2 \
        and database.teachers_of_subject(3) == 0, \
            "teachers_of_subject() incorrect"

    # select_teacher
    database.select_teacher(100001, 990101)
    database.select_teacher(100002, 990101)
    database.select_teacher(100003, 990102)
    database.select_teacher(100004, 990201)
    assert database.students[0].teacher.number == 990101 \
        and database.students[1].teacher.number == 990101 \
        and database.students[2].teacher.number == 990102 \
        and database.students[3].teacher.number == 990201, \
            "select_teacher() incorrect"
    database.select_teacher(100005, 990301)
    assert database.students[4].teacher is None, \
        "select_teacher() didn't consider whether the teacher is not in the database"

    # students_of_teacher
    assert database.students_of_teacher(990101) == 2 \
        and database.students_of_teacher(990102) == 1 \
        and database.students_of_teacher(990201) == 1 \
        and database.students_of_teacher(990202) == 0, \
            "students_of_teacher() incorrect"
    database.select_teacher(100006, 990101)
    assert database.students_of_teacher(990101) == 2, \
        "select_teacher() didn't consider whether the student is not in the database"
    assert database.students_of_teacher(990301) < 0, \
        "students_of_teacher() didn't consider whether the teacher is not in the database"

    # teacher_of_student
    assert database.teacher_of_student(100001) == 0 \
        and database.teacher_of_student(100002) == 0 \
        and database.teacher_of_student(100003) == 1 \
        and database.teacher_of_student(100004) == 2, \
            "teacher_of_student() incorrect"
    assert database.teacher_of_student(100005) < 0, \
        "teacher_of_student() didn't consider whether the student hasn't choose any teacher"
    assert database.teacher_of_student(100006) < 0, \
        "teacher_of_student() didn't consider whether the student is not in the database"    
    assert database.teacher_of_student(990301) < 0, \
        "teacher_of_student() didn't consider whether the teacher is not in the database"

    # students_of_subject
    assert database.students_of_subject(1) == 3 \
        and database.students_of_subject(2) == 1 \
        and database.students_of_subject(3) == 0, \
            "students_of_subject() incorrect"

    # popular_teacher
    assert database.popular_teacher() == 2, \
        "popular_teacher() incorrect"

    # popular_subject
    assert database.popular_subject() == 3, \
        "popular_subject() incorrect"

    # unselected_teachers
    assert database.unselected_teachers() == 1, \
        "unselected_teachers() incorrect"

    # unselected_students
    assert database.unselected_students() == 1, \
        "unselected_students() incorrect"

    # delete_student
    database.delete_student(100001)
    assert database.nb_students() == 4 \
        and database.student_index_by_id(100002) == 0, \
            "delete_student() incorrect"

    # delete_teacher
    database.delete_teacher(990201)
    assert database.nb_teachers() == 3 \
        and database.teacher_index_by_number(990202) == 2, \
            "delete_teacher() incorrect"
    assert database.students[2].teacher is None, \
        "delete_teacher() didn't change students' status who choose this teacher"

    print(f"\n[Success]")


# main
test()
