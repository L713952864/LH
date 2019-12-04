"""一个可用于描述餐厅的类"""


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The restaurant's name: " + self.restaurant_name)
        print("The cuisine type: " + self.cuisine_type.lower())

    def open_restaurant(self):
        print("This restaurant is opening!")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, full_served):
        self.number_served += 1
        if self.number_served >= full_served:
            print("FULL SERVED!")

