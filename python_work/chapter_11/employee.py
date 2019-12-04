"""一个名为Employee的类"""


class Employee:
    def __init__(self, first_name, last_name, income):
        self.first_name = first_name
        self.last_name = last_name
        self.income = income

    def give_raise(self, add=5000):
        self.income = self.income + add

    def show_employee(self):
        print(self.first_name + " " + self.last_name + ":")
        print("\t" + self.income)