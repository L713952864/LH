"""类的继承 test:9-6"""
from restaurant import Restaurant


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        """初始化父类的属性，再初始化子类特有属性"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['coco', 'rose']

    def iceream_display(self):
        print("Icecream's flavors: " + str(self.flavors))

    def open_restaurant(self):
        """重写父类方法"""
        print("This IceCreamStand is opening!")

def main():
    icecream_stand = IceCreamStand('VCOS', 'icecream')
    icecream_stand.describe_restaurant()
    icecream_stand.iceream_display()
    icecream_stand.open_restaurant()
    pass


if __name__ == '__main__':
    main()