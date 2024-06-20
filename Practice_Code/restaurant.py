class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'The name of the restaurant is {self.name} and they serve {self.cuisine_type} type of food.')

    def open_restaurant(self):
        print(f'The restaurant {self.name} is now open.')
        

first_restaurant = Restaurant('Taste of India', 'Indian')
second_restaurant = Restaurant('McDonalds', 'Fast food')
third_restaurant = Restaurant('La Rochelle', 'Mexican')


first_restaurant.describe_restaurant()
second_restaurant.describe_restaurant()
third_restaurant.describe_restaurant()