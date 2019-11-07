from socket import *
from time import ctime

host = 'XXX.XXX.XXX.XXX'
port = 5566
buffsize = 1024
addr = (host, port)
def main():
    tcp_server_socket = socket(AF_INET, SOCK_STREAM)
    tcp_server_socket.bind(addr)
    tcp_server_socket.listen(15)
    while True:
        print('waiting for connection...')
        tcp_client_socket, client_addr = tcp_server_socket.accept()
        print('...connected from:', client_addr)

        while True:
            recvmsg = tcp_client_socket.recv(buffsize)
            msg = recvmsg.decode('utf-8')
            if msg == 'q':
                break
            print('receive:' + msg)
            sendmsg = input('reply:')
            tcp_client_socket.send(sendmsg.encode('utf-8'))
    tcp_server.socket.close()



if __name__ == '__main__':

    main()