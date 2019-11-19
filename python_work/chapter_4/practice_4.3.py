"""
4.5
元组：不可变的列表
"""
def main():
    print("original buffet:")
    buffet = ('cookies', 'coke', 'chicken', 'noodles', 'beef')
    for food in buffet:
        print(food)

    print('\n')
    print("modified buffet:")
    buffet = ('cookies', 'orange juice', 'bacon', 'noodles', 'chicken')
    for food in buffet:
        print(food)


    pass
if __name__ == '__main__':
    main()