"""函数:形参和实参"""


def display_message():
    print("I HAVE BEEN LEARNING FUNCTION")


def favorite_book(title):
    print("One of my favorite book is " + title + '.')


def make_shirt(size, pic = 'I love Python'):
    print("This shirt's size is " + str(size) + ", and the pic is " + pic + ".")


def describe_city(name, country = 'China'):
    print(name + " is in " + country + '.')


def main():
    # display_message()
    # favorite_book('Der Steppenwolf')
    make_shirt(24, 'dog')  # 位置实参
    make_shirt(size=34, pic='cat')  # 关键字实参
    make_shirt(size=55)

    describe_city('Reykjavik', 'Iceland')
    describe_city('Beijing')
    describe_city(country='France', name='Paris')
    pass


if __name__ == '__main__':
    main()