"""存储数据
    json.dump(): 存储数据，接受两个实参：要存储的数据以及可用于存储数据的文件对象。
    json.load()
"""
import json
filename = 'favorite_number.json'


def new_f_number():
    try:
        username = input("Hello. What is your name?")
        number_input = input("What is your favorite number?")
        f_number = int(number_input)
        favorite_number = {username: f_number}
        with open(filename, 'a') as f_number_obj:
            json.dump(favorite_number, f_number_obj)
        return favorite_number
    except ValueError:
        print("What you input is not a number!")


def get_f_number():
    try:
        with open(filename) as f_number_obj:
            data = json.load(f_number_obj)
    except FileNotFoundError:
        return new_f_number()
    else:
        return data


def greet_user():
    name = input("What is your name?")
    flag = True
    for username in get_f_number().keys():
        if username == name:
            print(username + ", I know your favorite number is " + str(get_f_number()[username]))
            flag = False
            break
    if flag:
        print("you are new here.")


def main():
    greet_user()
    pass


if __name__ == '__main__':
    main()