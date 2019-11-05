"""
构造程序逻辑 && 函数与模块

from FILE_A import foo
from FILE_B import foo
foo() #同一命名，进行覆盖
"""
import FILE_A as first
import FILE_B as second

def main():
    first.foo()
    second.foo()

    pass
if __name__ == '__main__':
    main()
