"""
while用于字典和列表
"""
def main():
    sandwich_orders = ['pastrami', 'tuna sandwich', 'pastrami', 'mango sandwich', 'pastrami', 'chicken sandwich']
    print(sandwich_orders)
    print("pastrami sold out.")
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    finished_sandwiches = []
    while sandwich_orders:
        sandwich = sandwich_orders.pop();
        print("I made your " + sandwich)
        finished_sandwiches.append(sandwich)
    print(finished_sandwiches)

    flag = True
    visit = {}
    while flag:
        name = input("What's your name?")
        place = input("If you could visit one place in the world, where would you go?")
        visit[name] = place
        repeat = input("go on?(yes/no)")
        if repeat == 'no':
            flag = False
    for name, place in visit.items():
        print(name.title() + " want to visit " + place.title())
    pass
if __name__ == '__main__':
    main()