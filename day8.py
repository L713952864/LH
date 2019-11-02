"""
面向对象
"""
from math import sqrt
from time import time, localtime, sleep

class Student(object):
    # 限定该类对象只能绑定以下三个属性，只对当前类的对象生效，对子类无效
    __slots__ = ('name', '_age', '_gender')
    def __init__(self, name='A', age=0):
        self.name = name
        self._age = age #private

    @property #通过装饰器property中的访问器：getter方法
    def age(self):
        return self._age
    @age.setter #修改器：setter方法
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s is playing with toys.' % self.name)
        else:
            print('%s is playing whatever he like.' % self.name)

    def study(self, course):
        print('%s 在学 %s .' % (self.name, course))

    def __bar(self): #private
        print(self._age)
        print('__bar')

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

"""数字时钟"""
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
def main():
    stu1 = Student('Z', 10)
    stu1.study('abc')
    stu1.age = 12
    stu1.play()
    stu1._gender = 'female'
    # stu1._is_gay = True 报错，如果没有slot绑定，可以动态绑定另加属性
    # stu1.__bar() #AttributeError bar()私有，访问不了
    stu1._Student__bar() #换个名字又可以访问，私密性不足
    # print(stu1._Student__age)

    a, b = 2, 2
    if Point.is_valid(a, b):
        p1 = Point(a, b)
    else:
        print('Please enter again...')
    p2 = Point()
    p2.move_by(-2, 8)
    print(p2) #调用的实际是__str__(self)
    print(p1.distance_to(p2))

    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()

if __name__ == '__main__':
    main()