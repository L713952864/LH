from user import User


class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("The privileges of admin:")
        for privilege in self.privileges:
            print("\t-" + privilege)


class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        """将Privileges实例用作其属性"""
        self.privileges = Privileges()