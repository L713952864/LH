"""test:9-7"""
from admin import Admin


def main():
    admin = Admin('Hazel', 'Albert', 33)
    admin.privileges.show_privileges()


if __name__ == '__main__':
    main()
