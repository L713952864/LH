"""
字典
"""
def main():
    # 人以及最喜欢的数字
    favorite_number = {
        'Lily': 3,
        'Sarah': 5,
        'Jerry': 78,
        'Moris': 33,
        'jeff': 33,
    }
    query = ['Lily', 'Moris', 'Wuang']
    for name, number in favorite_number.items():
        print("\n" + name + "'s favorite number is " + str(number))
    for name in sorted(favorite_number.keys()):
        print(name)
    for number in set(favorite_number.values()):
        print(number)
    for people in query:
        if people in favorite_number.keys():
            print("Thanks for accepting the investigation, " + \
                  people.title()
                  )
        else:
            print("Please complete this investigation with us, "\
                  + people.title()
                  )

    # Python术语字典
    dictionary = {
        'class': '类',
        'def': '定义函数',
    }
    print('def:' + dictionary['def'])

    geography = {
        'nile': 'egypt',
        'the Volga': 'russia',
        'the Danube': 'germany'
    }
    for river, country in geography.items():
        print(river.title() + ' runs through ' + country.title())
    for river in geography.keys():
        print(river)
    for country in geography.values():
        print(country)
    pass
if __name__ == '__main__':
    main()