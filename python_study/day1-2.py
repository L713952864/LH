import math
def main():

    def circle():
        radius = float(input('The radius of this circle is: '))
        perimeter = 2 * math.pi * radius
        print('The perimeter is %.2f' % perimeter)

    def number():
        a = 321
        b = 123
        print(a / b)
        print(a // b)
        print(a % b)
        print(a ** b)
        d = 'hell'
        e = "0" #只有使用特殊字符时才会有差别（"与'）
        a = int(input('a = '))
        b = int(input('b = '))
        print(type(d)) #使用type()对变量进行检查
        print(ord(e)) #使用ord()将字符串/一个字符转换成对应的编码
        print('%d + %d = %d' % (a, b, a + b))
        flag = not (1 != 2)
        print('flag = ', flag)
        print(flag is False) #False True 注意首字母大写

    def IsLeapYear():
        year = int(input('请输入年份: '))
        #如果代码太长写成一行不便于阅读 可以使用\对代码进行折行
        is_leap = (year % 4 == 0 and year % 100 != 0) or \
              year % 400 == 0
        print(is_leap)
    pass
if __name__ == '__main__':
    #input() #在命令行窗口press enter关闭窗口
    main()