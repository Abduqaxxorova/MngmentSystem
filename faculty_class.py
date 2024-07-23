from user_class import User
from abc import ABC, abstractmethod
position = {"TEACHING ASSISTANTS": 100,
            "LECTURERS": 150,
            "SENIOR LECTURERS": 200,
            "ASSISTANT PROFESSOR": 250,
            "ASSOCIATE PROFESSOR": 300,
            "FULL PROFESSOR": 350,
            "ACADEMICIAN": 400}
courses = ["it", "management", "math", "python"]
class Faculty(User):
    def __init__(self, type, name, pass_id, email, birth_dt, gender, nationality, phone, course, occupation, hours, salary, title):
        super().__init__(self, type, name, pass_id, email, birth_dt, gender, nationality, phone)
        self.set_course(course)
        self.set_occupation(occupation)
        self.set_hours(hours)
        self.set_salary(salary)
        self.set_title(title)
    @abstractmethod
    def teacher(self,ABC):
        pass


    def set_course(self,course):
        if course.lower() in courses:
            self.__course = course
        else:
            raise ValueError("We don't have this kind of courses!")

    def set_occupation(self,occupation):
        if occupation.lower() == "full-time" or occupation.lower() == "part-time":
            self.__occupation = occupation
        else:
            raise ValueError("We don't have this kind of occupation!")


    def set_hours(self, hours):
        extra_hours = 0
        hours = hours.strip()
        if hours.isnumeric():
            if self.get_occupation() == 'full-time':
                if hours > 24:
                    raise ValueError("It's illegal")
                elif 19 <= hours <= 24:
                    self.__hours = 18
                    self.__extra_hours = hours - 18
                elif 2 <= hours <= 18:
                    self.__hours = hours
                    self.__extra_hours = 0
                else:
                    raise ValueError("You are not working at all")
            elif self.get_occupation() == 'part-time':
                if hours > 12:
                    raise ValueError("It's illegal")
                elif 10 <= hours <= 12:
                    self.__hours = 9
                    self.__extra_hours = hours - 9
                elif 1 <= hours <= 9:
                    self.__hours = hours
                    self.__extra_hours = 0
                else:
                    raise ValueError("You are not working at all")

    def set_salary(self,salary):
        if salary.isnumeric():
            if self.get_title() in salary.keys():
                self.__salary = self.get_hours() * position[self.get_title()]
                self.__salary += self.__extra_hours * position[self.get_title()] * 0.5
            else:
                raise ValueError("We don't have this kind of title!")
            if self.get_occupation() == "part-time":
                self.__salary = self.__salary / 2
        else:
            raise ValueError("Salary should be numeric!")


    def set_title(self,title):
        if title.upper() in position.keys():
            self.__title = title
        else:
            raise ValueError("We don't have this kind of title!")



    def get_course(self):
        return self.__course

    def get_occupation(self):
        return self.__occupation

    def get_hours(self):
        return self.__hours

    def get_salary(self):
        return self.__salary

    def get_title(self):
        return self.__title

class Teaching_ass(Faculty):
    def teacher(self, user):
        print(f"{self.get_course()} is teaching {user.get_name()}")

class Lecturers(Faculty):
    def teacher(self, user):
        print(f"{self.get_course()} is lecturing {user.get_name()}")

class Senior_lecturers(Faculty):
    def teacher(self, user):
        print(f"{self.get_course()} is lecturing {user.get_name()}")

class Assistant_proff(Faculty):
    def teacher(self, user):
        print(f"{self.get_course()} is teaching {user.get_name()}")
class Associate_proff(Faculty):
    def teacher(self, user):
        print(f"{self.get_course()} is teaching {user.get_name()}")
class Full_proff(Faculty):
    def teacher(self, user):
        print(f"{self.get_course()} is teaching {user.get_name()}")
class Academician(Faculty):
    def teacher(self, user):
        print(f"{self.get_course()} is teaching {user.get_name()}")


course = input("Please enter your course name:")
occupation = input("Please enter your occupation (full-time/part-time):")
hours = int(input("Please enter your working hours:"))
salary = int(input("Please enter your salary:"))
title = input("Please enter your title:")
