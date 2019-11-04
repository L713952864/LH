"""
使用正则表达式
"""
import re
def instance_1():
    while True:
        username = input('please enter into your username:')
        qq = input('please enter into your qq number:')
        m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
        m2 = re.match(r'^[1-9]\d{4,11}$', qq)
        """
        match(pattern, string, flags=0)用正则表达式匹配字符串
        r'原始字符串' 字符串中没有所谓的转义字符
        ^表示开头 $表示结尾 [1-9]表示选择范围 {6,20} 表示重复次数
        \d表示匹配数字 \d{4,11}表示重复4到11次的数字
        """
        if not m1:
            print('please enter into valid username.')
            continue
        if not m2:
            print('please enter into valid qq number.')
            continue
        if m1 and m2:
            print("It's valid.")
            break
def instance_2():
    pattern = re.compile(r'(?<=\D)(1[38]\d{9}|14[57]\d{8}|15[0-35-9]\d{8}|17[678]\d{8})(?=\D)')
    """
    compile(pattern, flags=0)编译正则表达式返回正则表达式对象
    findall(pattern, string, flags=0)查找所有，返回字符串列表
    \D表示匹配非数字 (?<=\D)表示匹配非数字后面的位置 (?=\D)表示匹配非数字前面的位置
    """
    sentence = '''
        重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''
    mylist = re.findall(pattern, sentence)
    # print(mylist)
    #通过迭代器匹配对象，获得匹配内容
    for temp in pattern.finditer(sentence):
        print(temp.group())
    # 正则表达式一个括号一个group，group(0)同group()，返回整体
    string = "123abc456"
    print(re.search(r'([0-9]*)([a-z]*)([0-9]*)', string).group(2))  # *表示匹配0次或多次

    # search(string)搜索字符串中第一次出现正则表达式的模式，成功则返回匹配对象，否则返回None
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())

def substitute_bad():
    sentence = 'bad awful noisy word, good or bad mood.'
    purified = re.sub(r'[擦靠]|bad|awful', '*', sentence, flags=re.IGNORECASE)
    print(purified)

def split_long_string():
    with open('F:\昆明湖.txt', 'r', encoding='utf-8') as file:
        file_sentence = file.read()
        sentence_list = re.split(r'[, . ， 。]', file_sentence) # 以指定模式分隔符拆分字符串
        while '' in sentence_list:
            sentence_list.remove('')
        print(sentence_list)

def main():
    split_long_string()

if __name__ == '__main__':
    main()