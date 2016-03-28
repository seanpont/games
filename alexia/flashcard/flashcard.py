from random import shuffle


class Flashcards():
  def __init__(self):
    self.questions_answers = {}

  def read_file(self):
    f = open("mini_data.txt")
    for line in f:
      part = line.split(":")
      question = part[0].strip()
      answer = part[1].strip()
      self.questions_answers[question] = answer

  def game_play(self):
    questions = self.questions_answers.keys()
    shuffle(questions)
    count = 0
    for question in questions:
      answer_user = raw_input(question + " ")
      if answer_user == self.questions_answers[question]:
        count += 1
        print "Correct"
      else:
        print "Incorrect. The correct answer is", self.questions_answers[question]

    print count, "/", len(questions)
    print float(count) / len(questions)


flashcard = Flashcards()
flashcard.read_file()
flashcard.game_play()
