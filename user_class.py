from datetime import date

type_list = ["student", "staff", "teacher"]
class User:
    def __init__(self, type, name, pass_id, email, birth_dt, gender, nationality, phone):
        self.set_type(type)
        self.set_name(name)
        self.set_pass_id(pass_id)
        self.set_email(email)
        self.set_birth_dt(birth_dt)
        self.set_gender(gender)
        self.set_nationality(nationality)
        self.set_phone(phone)

    def set_type(self, type):
        if type.lower() in type_list:
            self.__type = type
        else:
            raise ValueError("Type should be one of the following: student, teacher, staff")

    def set_name(self, name):
        if name.isalpha() and len(name)>=2:
            self.__name = name
        else:
            raise ValueError("Name should be a string with at least 2 alphabetic characters")

    def set_pass_id(self,pass_id):
        if len(pass_id) == 9 and pass_id[:2].isalpha() and pass_id[2:].isdigit():
            self.__pass_id = pass_id
        else:
            raise ValueError("Pass ID incorrect!")

    def set_email(self,email):
        if "@" in email and "." in email:
            self.__email = email
        else:
            raise ValueError("Email incorrect!")

    def set_birth_dt(self,birth_dt):
        if 0<int(birth_dt[:2])<=31 and 0<int(birth_dt[3:5])<=12 and int(birth_dt[7:]) <= date.today().year:
            self.__birth_dt = birth_dt
        else:
            raise ValueError("Birth date incorrect!")

    def set_gender(self,gender):
        if gender.lower() == "male" or gender.lower() == "female":
            self.__gender = gender
        else:
            raise ValueError("Gender should be male or female")

    def set_nationality(self,nationality):
        if nationality.isalpha():
            self.__nationality = nationality
        else:
            raise ValueError("Nationality is incorrect!")
    def set_phone(self,phone):
        if phone[:3] == "998" and len(phone) == 12:
            self.__phone = phone
        else:
            raise ValueError("Phone number incorrect!")

    def get_type(self):
        return self.__type
    def get_name(self):
        return self.__name
    def get_pass_id(self):
        return self.__pass_id
    def get_email(self):
        return self.__email
    def get_birth_dt(self):
        return self.__birth_dt
    def get_gender(self):
        return self.__gender
    def get_nationality(self):
        return self.__nationality
    def get_phone(self):
        return self.__phone


type = input("Please enter your position (teacher, student, staff):")
name = input("Please enter your name: ")
pass_id = input("Please enter your passport ID (AB1234567):")
email = input("Please enter your email (myemail@gmail.com): ")
birth_dt = input("Please enter your birth date (DD.MM.YYYY): ")
gender = input("Please enter your gender (male, female): ")
nationality = input("Please enter your nationality: ")
phone = input("Please enter your phone number (998XXXXXXXXX): ")

user = User(type, name, pass_id, email, birth_dt, gender, nationality, phone)
