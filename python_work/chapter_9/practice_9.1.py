"""class
创建类和使用实例
"""
from restaurant import Restaurant
from user import User


def main():
    restaurant = Restaurant("ROLL", 'chinese')
    restaurant.describe_restaurant()
    restaurant.open_restaurant()

    restaurant_two = Restaurant('HU FAMILY', 'Chinese')
    restaurant_three = Restaurant('FISH AND RICE', 'CHINESE')
    restaurant_two.describe_restaurant()
    restaurant_three.describe_restaurant()

    restaurant.number_served = 13  # 对类里的属性进行直接修改
    print(restaurant.number_served)
    restaurant.set_number_served(37)
    print(restaurant.number_served)
    restaurant.increment_number_served(39)
    restaurant.increment_number_served(39)
    print(restaurant.number_served)
    user1 = User('Lily', 'Albert', 23)
    user2 = User('Moris', 'Hamilton', 24)
    user3 = User('Jeff', 'Churchill', 27)
    user1.describe_user()
    user1.greet_user()
    user2.describe_user()
    user2.greet_user()
    user3.describe_user()
    user3.greet_user()

    user1.increment_login_attempts()
    user1.increment_login_attempts()
    print(user1.login_attempts)
    user1.reset_login_attempts()
    print(user1.login_attempts)
    pass


if __name__ == '__main__':
    main()