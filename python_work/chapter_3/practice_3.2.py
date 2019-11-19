"""关于列表的练习
    list.append('')
    list.insert(0, '')
    del list[0]
    list.pop(0)
    list.pop() 末尾
    list.remove['']
"""

def main():
    friend_list = ['li', 'zhang', 'liang', 'huang', 'zhou', 'tong', 'shi']
    print("共有" + str(len(friend_list)) + "位嘉宾！")
    def welcome():
        for person in friend_list:
            print("Welcome to you, " + person.title())

    print(friend_list)
    print(friend_list.pop(6) + " can't come!")
    friend_list.append('huang')

    welcome()
    print("I find another bigger table!")

    friend_list.insert(0, 'zhang')
    friend_list.insert(5, 'wang')
    friend_list.append('liang')
    welcome()

    print('only two persons could be invited.')
    while len(friend_list) > 2:
        print(friend_list.pop().title() + ", I am so sorry for the dinner.")

    welcome()
    while True:
        if len(friend_list) != 0:
            del friend_list[0]
        else:
            print('list is blank.')
            break
    # print(friend_list[-1]) index error
    pass
if __name__ == '__main__':

    main()
