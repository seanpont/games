#!/usr/bin/python
# coding=utf-8

import string
import socket


def find_index_where(arr, condition):
  for i, a in enumerate(arr):
    if condition(a):
      return i
  return -1


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
    self.board = [[' '] * size for _ in xrange(size)]
    self.p1, self.p2 = p1_token, p2_token
    self.p1 = GREEN + self.p1 + ENDC
    self.p2 = BLUE + self.p2 + ENDC
    self.turn = self.p1
    self.winner = None

  def __str__(self):
    lines = ['']
    lines.append('     ' + '   '.join(string.ascii_lowercase[:self.size]))
    lines.append('   ' + '—' * (self.size * 4 + 1))
    for i, row in enumerate(self.board):
      lines.append('%2d' % (i + 1) + ' | ' + ' | '.join(row) + ' | ' + str(i + 1))
      lines.append('   ' + '—' * (self.size * 4 + 1))
    lines.append('     ' + '   '.join(string.ascii_lowercase[:self.size]))
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
    # Test row
    if self.test_for_goal(self.board[row_index]):
      return True
    # Test column
    if self.test_for_goal([row[col_index] for row in self.board]):
      return True
    min_row = max(0, row_index - col_index)
    min_col = max(0, col_index - row_index)
    squares = self.size - max(min_row, min_col)
    if self.test_for_goal(
        [self.board[min_row + i][min_col + i] for i in xrange(squares)]):
      return True
    max_row = min(self.size, row_index + col_index)
    min_col = max(0, col_index - (self.size - row_index))
    if self.test_for_goal(
        [self.board[max_row - i][min_col + i] for i in xrange(squares)]):
      return True
    return False


def game_console():
  size = int(raw_input("Board size: "))
  goal = int(raw_input("How many in a row to win? "))
  p1 = raw_input("Player 1 token: ").strip()[0]
  p2 = raw_input("Player 2 token: ").strip()[0]

  game = Game(size, goal, p1, p2)
  print 'enter your move by typing the row and column, like this: 5e'
  while not game.winner:
    print "\x1b[2J\x1b[H"
    print game
    move = raw_input("%s : " % game.turn)
    game.play_turn(move)
  print "Player %s wins!" % game.winner


def game_host(size, goal, p1, port):

  # create an INET, STREAMing socket
  serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # bind the socket to a public host and a well-known port
  serversocket.bind((socket.gethostname(), port))
  # become a server socket
  # queue up as many as 5 connect requests before refusing outside connections
  serversocket.listen(5)

  print 'waiting for a connection...'
  connection, client_address = serversocket.accept()
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


def game_client(ip_addr, port, p2):
  connection = socket.create_connection((ip_addr, port))
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


def main_menu():
  print("""
  Welcome to Connect 5!
  1) Host game over LAN
  2) Connect to game over LAN
  3) Play Connect 5! (default)
  """)
  game_type = raw_input("Choice: ")
  if game_type == '1':
    size = int(raw_input("Board size: "))
    goal = int(raw_input("How many in a row to win? "))
    p1 = raw_input("Player 1 token: ").strip()[0]
    port = int(raw_input("Enter port number: ").strip())
    game_host(size, goal, p1, port)
  elif game_type == '2':
    ip_addr = raw_input("Enter host ip: ").strip()
    port = int(raw_input("Enter host port: ").strip())
    p2 = raw_input("Enter your token: ").strip()[0]
    game_client(ip_addr, port, p2)
  else:
    game_console()


if __name__ == '__main__':
  main_menu()





