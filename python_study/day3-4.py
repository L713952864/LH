#分支结构
def f1(x):
    x = float(input('x = '))
    if x > 1:
        y = 3 * x -5
    elif x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3
    print('f1(%.2f) = %.2f' % (x, y))
    #Flat is better than nested.

#输入三个边长，如果能构成三角形就计算周长和面积
def Istriangle(a, b, c):
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    if a + b > c and a + c > b and b + c > a:
        perimeter = a + b + c
        print('the perimeter of this triangle is: %f' % perimeter) #关于%f，自动保留6位小数
        h = perimeter / 2
        area =(h*(h-a)*(h-b)*(h-c))**0.5
        print('the area of this triangle is: %.2f' % area)
    else:
        print('The three parameters cant become a triangle')

#循环结构
def Cal_sum():
    sum = 0
    for x in range(101): #x从0到100，range(101)表示0到100共101个数的整数序列，range(100)表示0到99
        sum += x         #range(1,100)表示1到99的整数序列
    print(sum)           #range(1,100,2)表示1到99的奇数序列，2为步长

    counter = 0
    while True:
        counter += 1
        sum -= 5
        if counter == 7:
            break #break:终止所在循环 continue:放弃本次循环后续代码，直接进入循环下一轮
    print(sum)

def table():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('%d*%d=%d' % (i, j, i * j), end='\t') #注意格式 默认换行打印 此时每打印后接一个制表符
        print() #表示空一行
#test
def xandy():
    x = int(input('x = '))
    y = int(input('y = '))
    if x > y:
        x, y = y, x #两个值互换
    for factor in range(x, 0, -1):
        if(x % factor == 0 and y % factor == 0):
            print('%d与%d的最大公约数为：%d' % (x, y, factor))
        print('%d与%d的最小公倍数为：%d' % (x, y, x * y//factor))
        break
def main():
    xandy()
    pass
if __name__ == '__main__':
    main()