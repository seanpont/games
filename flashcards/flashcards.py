from random import shuffle


def clear_console():
  """
  Does not seem to work within pycharm, but it works in most terminal windows.
  """
  print "\x1b[2J\x1b[H"


class Flashcards:
  def __init__(self):
    self.questions_answers = {}

  def import_file(self, fname):
    with open(fname) as f:
      for line in f:
        question, answer = line.split(':')
        question = question.strip()
        answer = answer.strip()
        self.questions_answers[question] = answer

  def quiz(self):
    questions = list(self.questions_answers.keys())
    shuffle(questions)
    correct = 0
    for question in questions:
      answer = raw_input('%s: ' % question)
      if answer == self.questions_answers[question]:
        correct += 1
        print 'Correct!'
      else:
        print 'Correct answer: ' + self.questions_answers[question]

    total = len(questions)
    score = correct / float(total)
    print 'score: %s / %s (%s)' % (correct, total, score)

  def practice(self, questions=None):
    if questions is None:
      questions = list(self.questions_answers.keys())
    shuffle(questions)
    incorrect = []
    for question in questions:
      answer = raw_input('%s: ' % question)
      if answer == self.questions_answers[question]:
        print 'Correct!'
      else:
        print 'Correct answer: ' + self.questions_answers[question]
        incorrect.append(question)

    if not incorrect:
      print 'Nice job! You got them all right!'
    else:
      print "Let's practice some of the ones you got wrong"
      raw_input('Press Enter to continue...')
      clear_console()
      self.practice(incorrect)


if __name__ == '__main__':
  clear_console()
  flashcards = Flashcards()
  flashcards.import_file('./mini_data.txt')
  flashcards.quiz()
  # flashcards.practice()

































