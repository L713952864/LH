from socket import *

host = 'XXX.XXX.XXX.XXX'
port = 5566
buffsize = 1024
client_addr = (host, port)

def main():
    tcp_client_socket = socket(AF_INET, SOCK_STREAM)
    tcp_client_socket.connect(client_addr)
    while True:
        sendmsg = input('please enter into:')
        if sendmsg == 'q':
            break
        tcp_client_socket.send(sendmsg.encode('utf-8'))
        msg = tcp_client_socket.recv(buffsize)
        print(msg.decode('utf-8'))
    tcp_client_socket.close()

if __name__ == '__main__':
    main()