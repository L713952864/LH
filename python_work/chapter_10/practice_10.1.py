"""读取文件"""


def main():
    file_name = 'learning_python.txt'
    with open(file_name) as file_object:
        """
        读取整个文件
        whole_file = file_object.read()
        print(whole_file)
        
        遍历文件对象
        lines = file_object.readlines()
        for line in lines:
            print(line.rstrip())
        """
        lines = file_object.readlines()
        print(lines)
    first_string = ''
    for line in lines:
        first_string += line.rstrip()
    print(first_string)
    print(first_string.replace('Python', 'c++'))
    # first_string并没有改变
    pass


if __name__ == '__main__':
    main()