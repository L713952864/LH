from socket import socket
from json import loads
from base64 import b64decode

def main():
    client = socket()
    client.connect(('10', 5566))
    in_data = bytes()  # 定义一个保存二进制数据的对象
    data = client.recv(1024)
    while data:
        in_data += data
        data = client.recv(1024)
    my_dict = loads(in_data.decode('utf-8'))
    filename = my_dict['filename']
    filedata = my_dict['filedata'].encode('utf-8')
    with open('E:/LH/' + filename, 'wb') as f:
        f.write(b64decode(filedata))
    print('completed.')

if __name__ == '__main__':
    main()