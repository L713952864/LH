"""从一个模块里导入多个类"""
from car import ElectricCar
import car
# from car import Car, ElectricCar


def main():
    my_tesla = ElectricCar('tesla', 'model s', 2016)
    print(my_tesla.get_descriptive_name())
    my_tesla.battery.describe_battery()
    my_tesla.battery.get_range()
    my_tesla.battery.upgrade_battery()
    my_tesla.battery.get_range()

    """导入整个模块，使用语法module_name.class_name访问需要的类"""
    my_beetle = car.Car('volkswagen', 'beetle', 2016)
    print(my_beetle.get_descriptive_name())
pass


if __name__ == '__main__':
    main()