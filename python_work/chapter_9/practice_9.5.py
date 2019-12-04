"""使用Python标准库，导入已有的模块"""
from collections import OrderedDict
from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)


def main():
    dictionary = OrderedDict()

    dictionary['class'] = '类'
    dictionary['def'] = '定义函数'
    print("术语解释")
    for noun, description in dictionary.items():
        print('\t' + noun + ': ' + description)

    dice_six_sides = Die()
    dice_ten_sides = Die(10)
    dice_twenty_sides = Die(20)
    num1 = []
    num2 = []
    num3 = []
    num = [num1, num2, num3]
    for i in range(0, 10):
        num1.append(dice_six_sides.roll_die())
        num2.append(dice_ten_sides.roll_die())
        num3.append(dice_twenty_sides.roll_die())

    print(num)



if __name__ == '__main__':
    main()