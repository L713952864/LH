"""异常"""


def main():
    while True:
        try:
            num1 = input("Please input a number:")
            num2 = input("Please input a number:")
            num = int(num1) + int(num2)
        except ValueError:
            print("It is not a number!")
        else:
            print(num)
    pass


if __name__ == '__main__':
    main()

"""
TypeError: 传入参数不符合预期的时候被抛出
ValueError: 当参数类型正确但数值不恰当时被抛出
"""
