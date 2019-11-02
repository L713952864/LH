"""
面向对象 封装 继承 多态
"""
from math import sqrt
from time import time, localtime, sleep
from abc import ABCMeta, abstractmethod

class Person(object, metaclass=ABCMeta):
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self._age = age # private
    @abstractmethod
    def make_voice(self):
        pass

class Teacher(Person):
    __slots__ = ('id', 'name', '_age', 'teacher_id')
    def __init__(self, id, name, age, teacher_id):
        super().__init__(id, name, age)
        self.teacher_id = teacher_id
    def make_voice(self):
        print('%s is a teacher.' % self.name)

class Student(Person):
    # 限定该类对象只能绑定以下三个属性，只对当前类的对象生效，对子类无效
    __slots__ = ('id', 'name', '_age', 'gender')
    @property #通过装饰器property中的访问器：getter方法
    def age(self):
        return self._age
    @age.setter #修改器：setter方法
    def age(self, age):
        self._age = age

    def make_voice(self):
        if self._age < 18:
            print('%s is a underage.' % self.name)
        else:
            print('%s is an adult.' % self.name)

    def study(self, course):
        print('%s is studying %s (Student).' % (self.name, course))
    def __bar(self):
        print('__bar')


# 继承：子类Junior 父类Student
class Junior(Student):
    # 限定该类对象只能绑定以下三个属性，只对当前类的对象生效，对子类无效
    __slots__ = ('id', 'name', 'age')
    def __init__(self, id, name, age, grade):
        super().__init__(id, name, age) #用父类属性 super()
        self._grade = grade
    @property
    def grade(self):
        return self._grade

    def make_voice(self):
        super().make_voice()
        print('子类make voice')
    def study(self, course):
        print('%s is studying %s' % (self.name, course))

"""
class Point(object):

    def __init__(self, x=1, y=1):
        self.x = x
        self.y = y

    @staticmethod #静态方法 类名调用
    def is_valid(x, y):
        return (isinstance(x, float) or isinstance(x, int)) and \
               (isinstance(y, float) or isinstance(y, int))

    def move_to(self, x, y):
        self.x = x
        self.y = y
    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy
    def distance_to(self, another):
        dx = self.x - another.x
        dy = self.y - another.y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))

#数字时钟
class Clock(object):
    def __init__(self, h=0, m=0, s=0):
        self._hour = h
        self._minute = m
        self._second = s

    @classmethod #类方法
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)
    # tm_hour属于time()方法里的


    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0
    def show(self):
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)
"""
def main():
    stu1 = Student(202, 'P', 10)
    stu1.study('English Grammer')
    stu1.age = 12
    stu1.make_voice()
    stu1._gender = 'female'
    # stu1._is_gay = True 报错，如果没有slot绑定，可以动态绑定另加属性
    # stu1.__bar() #AttributeError bar()私有，访问不了
    stu1._Student__bar() #换个名字又可以访问，私密性不足
    # print(stu1._Student__age)
    T = Teacher(333, 'T', 29, 1)
    T.make_voice()

    X = Junior(101, 'A', 20, 'grade one')
    X.make_voice()

    """
    a, b = 2, 2
    if Point.is_valid(a, b):
        p1 = Point(a, b)
    else:
        print('Please enter again...')
    p2 = Point()
    p2.move_by(-2, 8)
    print(p2) #调用的是__str(self)
    print(p1.distance_to(p2))

    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()
    """
if __name__ == '__main__':
    main()