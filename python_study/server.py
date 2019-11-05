from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
from json import dumps
from threading import Thread

class file_transfer_handler(Thread):
    def __init__(self, client):
        super().__init__()
        self.client = client
    def run(self):
        my_dict = {}

        with open('E:\LH\guido.jpg', 'rb') as f:
            my_dict['filename'] = 'guido.jpg'
            my_dict['filedata'] = b64encode(f.read()).encode('utf-8')
            json_str = dumps(my_dict)
        self.client.send(json_str.encode('utf-8'))
        self.client.close()

def main():
    server = socket()
    server.bind(('10', 5566))
    server.listen(512)
    while True:
        file_transfer_handler(server.accept()).start()

if __name__ == '__main__':
    main()