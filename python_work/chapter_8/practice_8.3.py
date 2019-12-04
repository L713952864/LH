"""函数：传递列表"""


def main():
    def sandwiches(*toppings):
        """topping是一个元组"""
        print("Make a sandwich with following toppings:")
        for topping in toppings:
            print("-" + topping)

    sandwiches('butter', 'strawberry')
    sandwiches('tuna')

    def build_profile(first, last, **user_info):
        """user_info是一个字典
            使用关键字实参
        """
        profile = {}
        profile['first_name'] = first
        profile['last_name'] = last
        for key, value in user_info.items():
            profile[key] = value
        return profile

    def show_profile(user_info):
        for key, value in user_info.items():
            print(key + ": " + str(value))
    user_profile = build_profile('Lily', 'Albert', age=12, sex='male', location='LA')
    show_profile(user_profile)

    def make_car(manufacturer, type, **car_info):
        car = {}
        car['manufacturer'] = manufacturer
        car['tyoe'] = type
        for key, value in car_info.items():
            car[key] = value
        return car

    car = make_car('subaru', 'outback', color='blue', tow_package=True)
    print(car)
    pass


if __name__ == '__main__':
    main()