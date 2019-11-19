"""
字典嵌套
练习 6.4
"""
def main():
    # 人的信息，将字典嵌套在列表里，为字典列表
    Lily = {
        'first_name': 'Lily',
        'last_name': 'Edward',
        'age': 23,
        'city': 'LA',
    }
    Jeff = {
        'first_name': 'Jeff',
        'last_name': 'Albert',
        'age': 22,
        'city': 'New York',
    }
    Moris = {
        'first_name': 'Moris',
        'last_name': 'Edwin',
        'age': 26,
        'city': 'Philadelphia',
    }
    people_information = [Lily, Jeff, Moris]
    for people in people_information:
        print(people)

    pp = {
        'species': 'dog',
        'owner': 'Lily',
    }
    kitty = {
        'species': 'cat',
        'owner': 'Moris',
    }
    black = {
        'species': 'rabbit',
        'owner': 'Jeff',
    }
    pets = [pp, kitty, black]
    for pet in pets:
        print(pet)

    # 在字典中嵌套列表
    like_place = {
        'Lily': ['LA', 'Tokyo'],
        'Moris': ['Beijing', 'Seoul', 'Tokyo'],
        'Jeff': ['Singapore'],
    }
    for person, places in like_place.items():
        print(person.title() + ' like ')
        if len(places) > 1:
            for place in places:
                print(place)
        else: print(places[0])

    # 在字典中嵌套字典
    cities = {
        'LA': {
            'country': 'America',
            'population': '39,760 thousand',
            'fact': 'Los Angeles is also called City of Angels'
        },

        'New York': {
            'country': 'America',
            'population': '85,100 thousand',
            'fact': 'The largest city in the United States.'
        },

        'Paris': {
            'country': 'France',
            'population': '22,400 thousand',
            'fact': 'Paris is the capital of France.'
        },
    }
    for name, city_info in cities.items():
        print("The name of city is: " + name)
        print("\tcountry: " + city_info['country'])
        print("\tpopulation: " + city_info['population'])
        print("\tfact: " + city_info['fact'])
    pass
if __name__ == '__main__':
    main()