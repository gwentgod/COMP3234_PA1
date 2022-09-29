#!/usr/bin/env python3
from SocketBase import *


class Client(SocketBase):
    def __init__(self, argv):
        try:
            self.TARGET = (argv[1], int(argv[2]))
        except (IndexError, ValueError):
            logging.error(f'Usage: {argv[0]} <server_addr> <server_port>')
            exit(1)

        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(self.TARGET)
        except (OSError, ConnectionError):
            logging.exception('Failed starting socket')
            exit(1)

        super().__init__(client_socket, client_socket.getsockname())

        logging.debug(self)

    def login(self):
        while True:
            username = input('Please input your user name: ')
            password = input('Please input your user password: ')
            login_msg = f'/login {username} {password}'
            self.send_str(login_msg)
            res = self.recv_str()
            if res == '1001 Authentication successful':
                logging.info(res)
                break
            else:
                logging.error(res)

    def game(self):
        logging.debug(self)


def main(argv):
    client = Client(argv)
    client.login()
    client.game()


if __name__ == '__main__':
    main(sys.argv)
