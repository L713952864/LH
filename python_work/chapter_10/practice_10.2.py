"""写入文件"""


def main():
    name = input("Please input your name: ")
    with open('guest.txt', 'w') as file_object:
        file_object.write(name)

    flag = True
    while flag:
        guest_name = input('Input your name: ')
        print("Good evening, " + guest_name)
        with open('guest_book.txt', 'a') as file_obj:
            file_obj.write(guest_name + ' CHECKED\n')
    pass


if __name__ == '__main__':
    main()