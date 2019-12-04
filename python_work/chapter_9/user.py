"""一个可用于描述用户的类"""


class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print("The user's information is following:")
        print('\tName: ' + self.first_name + " " + self.last_name)
        print('\tAge: ' + str(self.age))

    def greet_user(self):
        print("Hello, " + self.first_name.title())

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
