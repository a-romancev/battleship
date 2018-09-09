import socket


class Connector:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.opponent = None

    def connect(self, hostname):
        self.sock.connect((hostname, 8080))
        self.opponent = self.sock

    def listen(self, hostname):
        self.sock.bind((hostname, 8080))
        self.sock.listen(1)
        self.opponent, _ = self.sock.accept()

    def close(self):
        self.sock.close()

    def receive_answer(self):
        answ = self.opponent.recv(1)
        return bool(answ[0])

    def receive_guess(self):
        guess = self.opponent.recv(2)
        return int(guess[0]), int(guess[1])

    def send_guess(self, x, y):
        self.opponent.sendall(bytes([x, y]))

    def send_answer(self, is_hit):
        self.opponent.sendall(bytes([is_hit]))
