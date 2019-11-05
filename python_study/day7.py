"""
字符串
列表
元组
集合
字典
"""

import sys
def main():
    s1 = r'hello, single quotes \n' #\n表示换行 前面加r后\不再表示转义
    s2 = "hello, double quotation marks \141\142\143\x61\x62\x63\n" * 2
    s3 = """
    这个可以折行
    """
    """
    print(s1, s2, s3, end='')
    print(s2[-3:-1]) # str[a:b:c]表示从str这个字符串里切片，从a开始（从0开始计数）到b-1，步长为c
    # 当c为负数，倒着数，从-1开始计数
    a, b = 5, 10
    print(f'{a} * {b} = {a * b}')
    
    len(str) #计算字符串长度
    str.captitalize() #首字母大写
    str.title() #每个单词首字母大写
    str.upper() #整个字符串大写
    str.find('or') #显示位置，没有就是-1,下同
    str.index('or')
    str.startswith('he') #是否以指定字符串开头
    str.endswith('a')
    str.center(50, '*') #将字符串以指定宽度居中并在两侧填充指定字符 还有rjust:靠右放置
    str.isdigit() #是否都由数字构成
    str.isalpha() #是否都以字母构成
    str.isalnum() #是否以数字和字母构成
    str.strip() #获得字符串修剪左右两侧空格之后的拷贝
    
    
    list1 = [1, 3, 5, 7, 100]
    for index in range(len(list1)): #用下标遍历
        print(list1[index])
    for elem in list1: #通过元素遍历
        print(elem)
    for index, elem in enumerate(list1):
        print(index, elem)
    list1.append(200) #list后面添加元素
    list1.insert(1,400) #1号位置（0开始）添加元素
    list1.extend([1000, 2000]) #合并列表，放list1后面，下同
    list1 += [1000, 2000]
    if 3 in list1: #移除元素3
        list1.remove(3) 
    list1.pop(0) #从指定位置删除元素
    list1.clear() #清空列表
    
    # sorted函数返回列表排序后的拷贝不会修改传入的列表
    list2 = ['orange', 'apple', 'pear', 'mango', 'strawberry']
    list3 = sorted(list2) #默认字母表顺序排序
    list4 = sorted(list2, reverse = True)
    list5 = sorted(list2, key = len) #根据字符串长度排序
    print(list2, '\n', list3, '\n', list4, '\n', list5, '\n')
    list2.sort(reverse = True)
    print(list2)
    
    #用列表生成表达式语法创建列表容器
    f = [x for x in range(1, 10)]
    print(f)
    f = [x + y for x in 'ABCD' for y in '12']
    print(f)
    f = [x ** 2 for x in range(1,10)]
    print(sys.getsizeof(f)) #查看对象占用内存的字节数
    print(f)

    def fib(n):
        a, b = 0, 1
        for _ in range(n):
           a, b = b, a + b
           yield a
    # 把a取过的所有值都放进生产器 fib(n) 里

    t = ('Hazel', 22, True, 'Bj')
    for member in t: #遍历元组中的值
        print(member)
    t = ('Esperanza', 22, True, 'Cq')
    # 元组中的元素无法修改，变量t重新引用新的元组 而不能直接t[0] = 'Sarah'
    #将元组转换成列表，此时可以修改元素
    person = list(t)
    person[0] = 'Hazel'
    #将列表转换成元组
    fruit_list = ['peach', 'avocado']
    fruit_tuple = tuple(fruit_list)
    print(fruit_list, fruit_tuple)

    set1 = {1, 2, 3, 3, 4}
    set2 = set(range(1, 10))
    set3 = {num for num in range(1, 30) if num % 3 == 0}
    set1.add(5)
    set2.update([11, 12])
    set2.discard(5)
    if 4 in set2:
        set2.remove(4)
    set2.pop() #集合里第一个

    print(set1 & set2) #交集 print(set1.intersection(set2))
    print(set1 | set2) #并集 print(set1.union(set2))
    print(set1 - set2) #差集 print(set1.difference(set2))
    print(set1 ^ set2) #并集的元素除去交集的元素 print(set1.symmetric_difference(set2))
    print(set2 <= set1) #判断set2是否为set1的子集 print(set2.issubset(set1))
    print(set1 >= set3) #判断set1是否为set3的超集 print(set1.issuperset(set3))
    """

    #字典的每个元素是键值对
    scores = {'key': 99, 'Li': 10, 'Han': 20}
    items1 = dict(one=1, two=2, three=3, four=4)
    items2 = dict(zip(['a', 'b', 'c'], '123')) #zip()将两个序列压成字典
    items3 = {num: num ** 2 for num in range(1, 6)}
    print(scores['key']) #通过键获取字典中对应的值 print(scores.get('key'))
    for key in scores:
        print(f'{key}: {scores[key]}')
    #字典中键值可更新
    scores['Li'] = 88
    scores['Huang'] = 77
    scores.update(Zhou=3, Shi=4)
    print(scores.popitem()) #删除字典中的元素，从末尾开始删除
    print(scores)
    print(scores.pop('Huang', 222)) #打印Huang对应的值 222仿佛无用
    scores.clear() #清空字典

    pass

if __name__ == '__main__':
    main()