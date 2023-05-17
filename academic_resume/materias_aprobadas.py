
class Semester():
    """This is the period of studies"""

    def __init__(self, cardinal, min_credits, max_credits, payment):
        self.cardinal = cardinal
        self.min_credits = min_credits
        self.maex_credits = max_credits
        self.payment = payment

class Department:

    def __init__(self, courses, seminars, lectures):
        self.courses = courses
        self.seminars = seminars
        self.lectures = lectures

class Basic_subject:
    """This is one of the three types of subject in which a student can enroll"""

    def __init__(self, name, department, professor, credits):
        '''Initialize the attributes of the class'''
        self.name = name
        self.department = department
        self.professor = professor
        self.credits = credits

    def enroll(self):
        print(f"You have been enrolled in {self.name}")

    def withdraw(self):
        print(f"You have withdrawed the course {self.name} ")

class Author:
    """This is one of the three types of subject in which a student can enroll"""

    def __init__(self, name, department, professor, credits):
        '''Initialize the attributes of the class'''
        self.name = name
        self.department = department
        self.professor = professor
        self.credits = credits

    def enroll(self):
        print(f"You have been enrolled in {self.name}")

    def withdraw(self):
        print(f"You have withdrawed the course {self.name} ")


class Course:
    """This is one of the three types of subject in which a student can enroll"""

    def __init__(self, name, department, professor, credits):
        '''Initialize the attributes of the class'''
        self.name = name
        self.department = department
        self.professor = professor
        self.credits = credits

    def enroll(self):
        print(f"You have been enrolled in {self.name}")

    def withdraw(self):
        print(f"You have withdrawed the course {self.name} ")


class Seminar():
    """This is one of the three types of subject in which a student can enroll"""

    def __init__(self, name, department, professor, credits):
        '''Initialize the attributes of the class'''
        self.name = name
        self.department = department
        self.professor = professor
        self.credits = credits

    def enroll(self):
        print(f"You have been enrolled in {self.name}")

    def withdraw(self):
        print(f"You have withdrawed the course {self.name} ")

class lecture():
    """This is one of the three types of subject in which a student can enroll"""

    def __init__(self, name, department, professor, credits):
        '''Initialize the attributes of the class'''
        self.name = name
        self.department = department
        self.professor = professor
        self.credits = credits

    def enroll(self):
        print(f"You have been enrolled in {self.name}")

    def withdraw(self):
        print(f"You have withdrawed the course {self.name} ")
