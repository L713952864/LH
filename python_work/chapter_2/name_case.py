"""
2019/11/8
字符串
"""


def main():
    name = input('please input into your name:')
    print("Hello " + name + ", would you like to learn some Python today?")
    print(name.title() + '\t' + name.upper() + '\t' + name.lower())
    famous_person = 'Albert Einstein'
    message = 'A person who never made a mistake never tried anything new.'
    print(famous_person + 'once said, "' + message + '"')
    print(name + '\n' + name.rstrip() + '\t' + name.lstrip() + '\n' + name.strip())
if __name__ == '__main__':
    main()