import random


class Student:
    """
    NOTE: Any variables declared up front should be class variables
    meaning they are shared across all instances (static variables)

    Instance variables can be defined in __init__ (like a constructor)

    The following code is not needed since these are instance
    variables

    name = ""
    nickname = ""
    student_ID = 0
    password = ""
    """

    # count = 0

    def __init__(self, name="undefined", nickname="undefined",
                 student_id="0", password="Test1234"):
        self.name = name
        self.nickname = nickname
        self.student_id = student_id
        self.password = password

    """
    This is how you do accessors and mutators to protect variables.
    There is also @variable.deleter
    """
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        has_caps = False
        has_lower = False

        if len(password) < 8:
            raise ValueError("Password must be 8 or more characters")

        for letter in password:
            if letter.isupper():
                has_caps = True
                break

        if has_caps is False:
            raise ValueError("Password must contain at least 1 upper case "
                             "letter")

        for letter in password:
            if letter.islower():
                has_lower = True
                break

        if has_lower is False:
            raise ValueError("Password must contain at least 1 lower case "
                             "letter")

        self._password = password

    def to_string(self):
        return "Student Name: {} Nickname: {} Student ID: {} Password: {}".\
            format(self.name, self.nickname, self.student_id, self.password)

if __name__ == "__main__":
   pass
