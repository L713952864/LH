"""练习10-8，10-9"""


def main():
    filename_1 = 'dogs.txt'
    filename_2 = 'the_ducks.txt'
    try:
        with open(filename_1) as dog_file:
            dog_lines = dog_file.readlines()
            for line in dog_lines:
                print(line.rstrip())
        with open(filename_2, 'r', encoding='utf-8') as duck_file:
            duck_lines = duck_file.readlines()
        duck_line = ''
        for line in duck_lines:
            duck_line += line
    except FileNotFoundError:
        """print("Sorry, we can't find this file.")"""
        print(" ")
    else:
        print(duck_line.lower().count('the'))
    pass


if __name__ == '__main__':
    main()