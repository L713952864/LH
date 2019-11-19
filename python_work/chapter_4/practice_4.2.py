"""
4.3
"""
import time
def main():
    for i in range(1, 21):
        print(i)

    numbers = list(range(1, 1000001))
    print(min(numbers))
    print(max(numbers))
    start = time.time()
    print(sum(numbers))
    end = time.time()
    print(end - start)

    for i in range(1, 21, 2):
        print(i)

    values = []
    for value in range(3, 31):
        if value % 3 == 0:
            values.append(value)
    print(values)

    squares = [value**3 for value in range(1, 11)]
    print(squares)
    pass

if __name__ == '__main__':
    main()