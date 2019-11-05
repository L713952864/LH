def foo():
    global a #指示foo函数中的变量a来自于全局作用域
             #  nonlocal b 表示变量b来自于嵌套作用域
    a = 10
    print('hello!')



if __name__ == '__main__':
    a = 100
    foo()
    print(a)