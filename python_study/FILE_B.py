import os
import time
import random
def foo():
    print('goodbye!')
def letters():
    content = 'Welcome to Python...'
    while True:
        os.system('cls') #os.system('clear')
        print(content)
        time.sleep(0.2) #休眠200毫秒
        content = content[1:] + content[0]

#生成指定长度的验证码
def generate_code(code_len):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code

#返回给定文件名的后缀名
def get_suffix(filename, has_dot=False):
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''

if __name__ == '__main__':
    #letters()
    print(generate_code(5))
    print(get_suffix('aaa.dfdf'))
