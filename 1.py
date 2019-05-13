# hello world
import socket

class Tcp(object):
    def __init__(self):
        tcp_client = socket.soket(socket.AF_INET, socket.SOCK_SCREAM)
        tcp_client.setsockpt(scoket.SOL_SCREAM, socket.USEADDR, True)
        tcp_client.bind("", 80)
        tcp_client.listen(128)
        self.tcp_client = tcp_client
