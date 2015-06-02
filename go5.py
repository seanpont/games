# coding=utf-8

import string

def find_index_where(arr, condition):
    for i, a in enumerate(arr):
        if condition(a):
            return i
    return -1


def in_a_row(param, turn):
    pass


class Game(object):
    def __init__(self, goal, board_size):
        self.goal = goal
        self.size = board_size
        self.board = [[' ']*board_size for _ in xrange(board_size)]
        self.p1, self.p2 = ' ', ' '
        self.turn = self.p1

    def print_board(self):
        print ''
        print '     ' + '   '.join(string.ascii_lowercase[:self.size])
        print '   ' + '—' * (self.size*4 + 1)
        for i, row in enumerate(self.board):
            print '%2d' % (i+1) + ' | ' + ' | '.join(row) + ' | ' + str(i+1)
            print '   ' + '—' * (self.size*4 + 1)
        print '     ' + '   '.join(string.ascii_lowercase[:self.size])
        print ''

    def play(self):
        print 'Welcome to Go5! Get %d in a row to win!' % self.goal
        print 'Player one: select your token'
        self.p1 = raw_input("Player 1: ").strip()[0]
        self.p2 = raw_input("Player 2: ").strip()[0]
        self.turn = self.p1
        print 'enter your move by typing the row and column, like this: 5e'
        while True:
            self.play_turn()

    def play_turn(self):
        self.print_board()
        play = raw_input("%s : " % self.turn)
        index = find_index_where(play, lambda char: char in string.lowercase)
        if index == -1:
            print 'please enter the row then the column, like this: 5d'
            return
        row = int(play[:index]) - 1
        col = string.ascii_lowercase.find(play[index:])
        if self.board[row][col] == ' ':
            self.board[row][col] = self.turn
            if self.winner(row, col):
                print 'Player %s wins!' % self.turn
                exit()
            self.turn = self.p2 if self.turn == self.p1 else self.p1
        else:
            print "That spot is taken!"

    def winner(self, row, col):
        # check row
        in_a_row(self.board[row], self.turn)
        return False


game = Game(4, 9)
game.play()












