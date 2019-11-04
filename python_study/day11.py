"""
r：读取（默认）
w: 写入（会先截断之前的内容）文件中之前的内容都会被覆盖
x: 写入，如果文件已经存在会产生异常
a: 追加，将内容写入到已有文件的末尾
b: 二进制模式
t: 文本模式（默认）
+: 更新（既可以读又可以写）
"""
import time
import json

def main():
    mydict = {
        'name': 'Hazel',
        'age': 10,
        'fruit': [
            {'name': 'apple', 'number': 12},
            {'name': 'pinapple', 'number': 2},
            {'name': 'peach', 'number': 1},
        ]
    }

    try:
        with open('F:\data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)

        with open('F:\data.json', 'r') as fss:
            data = json.load(fss)
            print(data)
            """
            json模块主要有四个比较重要的函数，分别是：
                dump - 将Python对象按照JSON格式序列化到文件中
                dumps - 将Python对象处理成JSON格式的字符串
                load - 将文件中的JSON数据反序列化成对象
                loads - 将字符串的内容反序列化成Python对象
            """

        f1 = open('F:\Dora_Maar.txt', 'r', encoding='utf-8')
        # print(f1.read())
        for line in f1:
            print(line, end='')
            time.sleep(0.5)
        """
        with open('F:\昆明湖.txt', 'a', encoding='utf-8') as kunminghu_file:
            kunminghu_file.write('\n\n')
            kunminghu_file.write('___蔌弦')
        with open('F:\make_face.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))
        with open('F:\Blank.jpg', 'wb') as fs2:
            fs2.write(data)
        """
    except IOError as ex:
        print(ex)
        print('读写文件时发生错误')
    except FileNotFoundError:
        print('无法打开指定文件')
    except UnicodeDecodeError:
        print('读取文件时解码错误')
    finally:
          if f1:
            f1.close()

if __name__ == '__main__':
 main()