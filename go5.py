#!/usr/bin/python
# coding=utf-8

import string
import socket


def find_index_where(arr, condition):
    for i, a in enumerate(arr):
        if condition(a):
            return i
    return -1


class bcolors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'


class Game(object):
    def __init__(self, size, goal, p1_token, p2_token):
        self.size = size
        self.goal = goal
        self.board = [[' ']*size for _ in xrange(size)]
        self.p1, self.p2 = p1_token, p2_token
        self.p1 = bcolors.GREEN + self.p1 + bcolors.ENDC
        self.p2 = bcolors.BLUE + self.p2 + bcolors.ENDC
        self.turn = self.p1
        self.winner = None

    def __str__(self):
        # noinspection PyListCreation
        lines = ['']
        lines.append('     ' + '   '.join(string.ascii_lowercase[:self.size]))
        lines.append('   ' + '—' * (self.size*4 + 1))
        for i, row in enumerate(self.board):
            lines.append('%2d' % (i+1) + ' | ' + ' | '.join(row) + ' | ' + str(i+1))
            lines.append('   ' + '—' * (self.size*4 + 1))
        lines.append('     ' + '   '.join(string.ascii_lowercase[:self.size]))
        lines.append('')
        return '\n'.join(lines)

    def play_turn(self, move):
        index = find_index_where(move, lambda char: char in string.lowercase)
        if index == -1:
            print 'please enter the row then the column, like this: 5d'
            return
        row = int(move[:index]) - 1
        col = string.ascii_lowercase.find(move[index:])
        if self.board[row][col] == ' ':
            self.board[row][col] = self.turn
            if self.has_won(row, col):
                self.winner = self.turn
            else:
                # flip turn
                if self.turn == self.p1:
                    self.turn = self.p2
                else:
                    self.turn = self.p1
        else:
            print "That spot is taken!"

    def test_for_goal(self, tokens):
        """
        :param tokens: a sequence of tokens
        :return: true if there are goal sequences of turn in a row
        """
        in_a_row = 0
        for token in tokens:
            if token == self.turn:
                in_a_row += 1
            else:
                in_a_row = 0
            if in_a_row == self.goal:
                return True
        return False

    def has_won(self, row_index, col_index):
        in_a_row = 0
        # test row
        row = self.board[row_index]
        if self.test_for_goal(row):
            return True
        col = [row[col_index] for row in self.board]
        if self.test_for_goal(col):
            return True
        return None


def game_console():
    size = raw_input("Board size: ")
    goal = raw_input("How many in a row to win? ")
    p1 = raw_input("Player 1 token: ").strip()[0]
    p2 = raw_input("Player 2 token: ").strip()[0]

    game = Game(goal, size, p1, p2)
    print 'enter your move by typing the row and column, like this: 5e'
    while not game.winner:
        print game
        move = raw_input("%s : " % game.turn)
        game.play_turn(move)
    print "Player %s wins!" % game.winner


def game_host():
    size = int(raw_input("Board size: "))
    goal = int(raw_input("How many in a row to win? "))
    p1 = raw_input("Player 1 token: ").strip()[0]

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (socket.gethostbyname(socket.gethostname()), 8000)
    print 'starting up on %s port %s' % server_address
    sock.bind(server_address)
    sock.listen(5)
    print 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        p2 = connection.recv(256).strip()
        print 'p2 token: ', p2
        game = Game(size, goal, p1, p2)
        connection.sendall('%s,%s,%s,%s' % (size, goal, p1, p2))
        while not game.winner:
            print game
            if game.turn == game.p1:
                move = raw_input("%s : " % game.turn)
                connection.sendall(move)
            else:
                move = connection.recv(64).strip()
            game.play_turn(move)
        print "Player %s wins!" % game.winner
    finally:
        connection.close()


def game_client():
    ip_addr = raw_input("Enter host ip: ").strip()
    p2 = raw_input("Enter your token: ").strip()[0]
    connection = socket.create_connection((ip_addr, 8000))
    try:
        connection.sendall(p2)
        data = connection.recv(256).strip()
        print data
        size, goal, p1, p2 = data.split(',')
        size, goal = int(size), int(goal)
        game = Game(size, goal, p1, p2)
        while not game.winner:
            print game
            if game.turn == game.p2:
                move = raw_input("%s : " % game.turn)
                connection.sendall(move)
            else:
                move = connection.recv(64).strip()
            game.play_turn(move)
        print "Player %s wins!" % game.winner
    finally:
        connection.close()


if __name__ == '__main__':
    import sys
    args = sys.argv
    if '-h' in args:
        game_host()
    elif '-c' in args:
        game_client()
    else:
        game_console()






