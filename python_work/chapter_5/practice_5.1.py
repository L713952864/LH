"""if:
conditional_test
"""

def main():
    numbers = [2, 4, 9, 34, 18, 17]
    print('Is there a number 7? I predict True.')
    print(7 in numbers)
    print("Is the smallest number 2 in numbers? I predict True.")
    print(min(numbers) == 2)

    str1 = 'Angel'
    str2 = 'Angle'
    print(str1 == str2)
    print(str1.lower() == 'angel')
    print(7<=8)
    print((5 in numbers) and (18 in numbers))
    print((4 not in numbers) or (34 in numbers))
    pass

if __name__ == '__main__':
    main()