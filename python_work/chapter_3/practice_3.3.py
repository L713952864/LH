def main():
    travel_list = ['Tokyo', 'Hongkong', 'London', 'New York', 'Port Elizabeth', 'Berlin']
    print(travel_list)
    print("使用 sorted()按字母顺序打印这个列表，再次打印该列表，核实排列顺序未变。 ")
    print(sorted(travel_list))
    print(travel_list)
    print(" 使用 sorted()按与字母顺序相反的顺序打印这个列表，再次打印该列表，核实排列顺序未变。 ")
    print(sorted(travel_list, reverse=True))
    print(travel_list)

    print("使用 reverse()修改列表元素的排列顺序。打印该列表，核实排列顺序确实变了。")
    travel_list.reverse()
    print(travel_list)
    print("使用 reverse()再次修改列表元素的排列顺序。打印该列表，核实已恢复到原来 的排列顺序。")
    travel_list.reverse()
    print(travel_list)

    print("使用 sort()修改该列表，使其元素按字母顺序排列。打印该列表，核实排列顺 序确实变了。 ")
    travel_list.sort()
    print(travel_list)
    print("使用 sort()修改该列表，使其元素按与字母顺序相反的顺序排列。打印该列表， 核实排列顺序确实变了。 ")
    travel_list.reverse()
    print(travel_list)


    pass
if __name__ == '__main__':
    main()