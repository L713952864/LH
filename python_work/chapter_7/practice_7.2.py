"""while"""
def main():
    flag = True
    while flag:
        topping = input("Please input topping of pizza which you like to add in: ")
        if topping == "quit":
            break;  # flag = False
        else:
            print("We will add " + topping + " into your pizza!")

    while flag:
        age = input("how old are you?")
        age = int(age)
        if age < 3:
            print("you are free for the cinema.")
        elif age <= 12:
            print("your ticket price is 10 dollars.")
        else:
            print("your ticket price is 15 dollars.")
    pass
if __name__ == '__main__':
    main()