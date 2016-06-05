from Tkinter import *
import random

LOSER_WINNER = {'r': 'p', 'p': 's', 's': 'r'}
WINNER_LOSER = {'r': 's', 's': 'p', 'p': 'r'}

class RoShamBobot:
  def __init__(self, seq_length=3):
    self.n = seq_length
    self.play_count = {}
    self.history = ''

  def play(self):
    r = random.choice('rps')
    if len(self.history) < self.n:
      return r
    last_m = self.history[-self.n + 1:]
    keys = [k for k in self.play_count.keys() if k.startswith(last_m)]
    if not keys:
      return r
    max_key = max(keys, key=lambda x: self.play_count[x])
    return LOSER_WINNER[max_key[-1]]

  def last_play(self, rps):
    self.history += rps
    if len(self.history) < self.n:
      return
    last_n = self.history[-self.n:]
    self.play_count[last_n] = self.play_count.get(last_n, 0) + 1

  def reset(self):
    self.play_count = {}
    self.history = ''


class RoShamBoGame:
  def __init__(self):
    self.p1_score = 0
    self.p2_score = 0

  def play(self, p1_rps, p2_rps):
    if p1_rps == p2_rps:
      return 0
    elif WINNER_LOSER[p1_rps] == p2_rps:
      self.p1_score += 1
      return 1
    else:
      self.p2_score += 1
      return 2

  def reset(self):
    self.p1_score = 0
    self.p2_score = 0


def rps_text(rps):
  return {'r': 'ROCK',
          'p': 'PAPER',
          's': 'SCISSORS'}.get(rps)


class App:
  def __init__(self):
    self.root = Tk()
    self.root.wm_title("Rock Paper Scissors")

    frame = Frame(self.root, padx=12, pady=12)
    frame.pack()

    self.robot_score_text = StringVar()
    self.robot_score_label = Label(frame, textvariable=self.robot_score_text)
    self.robot_score_label.grid(row=0, column=0, pady=8)

    self.human_score_text = StringVar()
    self.player_score_label = Label(frame, textvariable=self.human_score_text)
    self.player_score_label.grid(row=0, column=2, pady=8)

    self.robot_rps_text = StringVar()
    self.robot_rps_label = Label(frame, textvariable=self.robot_rps_text)
    self.robot_rps_label.grid(row=1, column=1, sticky='EW')

    self.human_rps_text = StringVar()
    self.human_rps_label = Label(frame, textvariable=self.human_rps_text)
    self.human_rps_label.grid(row=2, column=1, sticky='EW', pady=8)

    self.rock_button = Button(frame,
                              text="ROCK",
                              command=lambda: self.play('r'),
                              width=10)
    self.rock_button.grid(row=3, column=0, sticky='EW')

    self.paper_button = Button(frame,
                               text="PAPER",
                               command=lambda: self.play('p'),
                               width=10)
    self.paper_button.grid(row=3, column=1, sticky='EW')

    self.scissors_button = Button(frame,
                                  text="SCISSORS",
                                  command=lambda: self.play('s'),
                                  width=10)
    self.scissors_button.grid(row=3, column=2, sticky='EW')

    self.root.bind("<Left>", lambda e: self.play('r'))
    self.root.bind("<Up>", lambda e: self.play('p'))
    self.root.bind("<Down>", lambda e: self.play('p'))
    self.root.bind("<Right>", lambda e: self.play('s'))

    # create a menu
    menu = Menu(self.root)
    self.root.config(menu=menu)

    file_menu = Menu(menu)
    menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New Game", command=self.new_game)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=self.root.quit)

    self.robot = RoShamBobot(4)
    self.game = RoShamBoGame()
    self.new_game()

  def run(self):
    self.root.mainloop()
    try:
      self.root.destroy()
    except TclError:
      pass

  def play(self, rps):
    robot_rps = self.robot.play()
    won = self.game.play(rps, robot_rps)
    self.robot_rps_text.set(rps_text(robot_rps))
    self.human_rps_text.set(rps_text(rps))
    if won == 0:
      self.human_rps_label.configure(bg='white')
      self.robot_rps_label.configure(bg='white')
    elif won == 1:
      self.human_rps_label.configure(bg='green')
      self.robot_rps_label.configure(bg='red')
    elif won == 2:
      self.human_rps_label.configure(bg='red')
      self.robot_rps_label.configure(bg='green')
    self.human_score_text.set('Human: %s' % self.game.p1_score)
    self.robot_score_text.set('Robot: %s' % self.game.p2_score)
    self.robot.last_play(rps)

  def new_game(self):
    print 'new game'
    self.game.reset()
    self.robot.reset()
    self.robot_rps_text.set('READY')
    self.human_rps_text.set('READY')
    self.human_score_text.set('Human: %s' % self.game.p1_score)
    self.robot_score_text.set('Robot: %s' % self.game.p2_score)

App().run()
