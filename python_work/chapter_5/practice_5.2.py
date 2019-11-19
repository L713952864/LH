"""
if语句
练习5.3/5.4节
"""
def main():
    alien_color = 'red'
    if alien_color == 'green':
        print('FIVE points!')
    elif alien_color == 'yellow':
        print('TEN points!')
    elif alien_color == 'red':
        print('15 points!')
    pass

    age = 15
    if age < 2:
        print('you are a baby.')
    elif age < 4:
        print('come on, you are learning how to walk.')
    elif age < 13:
        print('you are a child.')
    elif age < 20:
        print('you are a youngster.')
    elif age < 65:
        print('you are an adult.')
    else:
        print('you are an old man.')

    fruits = ['peach', 'avocado', 'pear', 'pinapple']
    favorite_fruits = ['peach', 'avocado', 'pear']
    for fruit in fruits:
        if fruit in favorite_fruits:
            print('you really like ' + fruit + '!')
    print('\n')

    print('5-8/5-9/5-10')
    current_users = ['hazel', 'admin', 'esperanza', 'sarah', 'lily']
    new_users = ['Hazel', 'esperanza', 'Wik', 'eric', 'emma']
    if current_users:
        for user in current_users:
            if user == 'admin':
                print("Hello " + user + ", would you like to see a status report?")
            else:
                print("Hello " + user.title() + ', thank you for logging in again.')
    else:
        print('We need to find some users!')
    for user in new_users:
        if user.lower() in current_users:
            print('请输入别的用户名！')
        else:
            print("这个用户名未被使用。")

    print('\n 5-11 序数')
    list = [i for i in range(1, 10)]
    for num in list:
        if num == 1:
            print(str(num) + 'st')
        elif num == 2:
            print(str(num) + 'nd')
        elif num == 3:
            print(str(num) + 'rd')
        else:
            print(str(num) + 'th')





if __name__ == '__main__':
    main()