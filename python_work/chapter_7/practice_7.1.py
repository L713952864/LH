"""
用户输入和while循环
"""

def main():
    car_name = input("What kind of cars would you like to rent?")
    print("Let me see if I can find you a " + car_name + '.')

    dinner_num = input("How many people are having dinner?")
    if int(dinner_num) > 8:
        print("Sorry, no available table for dinner.")
    else:
        print("Yes, you could have dinner here.")

    number = input("Please enter a number:")
    if int(number) % 10 == 0:
        print("这个数字是10的整数倍。")
    else:
        print("这个数字不是10的整数倍。")
    pass

if __name__ == '__main__':
    main()