"""
操作列表
遍历
4.1/4.2/4.4
切片 副本
"""
def main():
    pizza_list = ['Super Special', 'Original Porchetta', 'Black Pepper Beef', 'New Orleans', 'Marinara']
    for pizza in pizza_list:
        print("I like " + pizza)
    print("I really like pizza!\n")

    animals = ['tiger', 'cat', 'panda', 'chimpanzee', 'hound', 'ostrich']
    for animal in animals:
        print("A " + animal + " has eyes.")
    print("They are all alive in this world\n")

    print("The first three items in the list are: " + str(animals[0:3]))
    print("Three items from the middle of the list are: " + str(animals[1:4]))
    print("The last three items in the list are: " + str(animals[-3:]))
    print("\n")
    friend_pizza = pizza_list[:]
    pizza_list.append('Caprese')
    friend_pizza.append('Aussie')
    print("My favorite pizzas are: " + str(pizza_list))
    print("My friend's favorite pizzas are: " + str(friend_pizza))
    pass
if __name__ == '__main__':
    main()
