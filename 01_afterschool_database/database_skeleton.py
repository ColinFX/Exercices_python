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
        
        # TODO
        pass
    
    # b) return number of students
    def nb_students(self):
        
        # TODO
        pass
    
    # c) return index of one teacher in teachers list by given job number
    def teacher_index_by_number(self, _number):
        
        # TODO
        pass
    
    # d) return index of one student in students list by given student id
    def student_index_by_id(self, _id):
        
        # TODO
        pass

    # e) add one teacher into the database
    def add_teacher(self, _name, _gender, _subject, _number):
        
        # TODO
        pass
    
    # f) add one student into the database
    def add_student(self, _name, _gender, _id):
        
        # TODO
        pass

    # g) return student / teacher ratio
    def ratio(self):

        # TODO
        pass

    # h) print list of teachers of a subject and return number of the teachers
    def teachers_of_subject(self, _subject):

        # TODO
        pass

    # i) let one student of given id select one teacher by given teacher job number
    def select_teacher(self, _id, _number):

        # TODO
        pass

    # j) print list of students of one teacher by given job number and return number of the students
    def students_of_teacher(self, _number):

        # TODO
        pass

    # k) return index of the teacher of one student by given id
    def teacher_of_student(self, _id):

        # TODO
        pass

    # l) print list of students of one subject and return number of the students
    def students_of_subject(self, _subject):

        # TODO
        pass

    # m) find most popular teacher in database and return the maximum number of students of that teacher
    def popular_teacher(self):

        # TODO
        pass

    # n) find most popular subject and return the maximum number of students of that subject
    def popular_subject(self):

        # TODO
        pass

    # o) print list of teachers with no student and return number of teachers
    def unselected_teachers(self):

        # TODO
        pass

    # p) print list of students with no teacher and return number of the students
    def unselected_students(self):

        # TODO
        pass

    # q) delete one student of given id from database
    def delete_student(self, _id):

        # TODO
        pass

    # r) delete one teacher of given number from database
    def delete_teacher(self, _number):

        # TODO
        pass


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
