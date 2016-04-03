from random import shuffle

data_file = open("data.txt")

Q_and_A = {}

print data_file

class Flashcards(object):

    def __init__(self):
        self.q_and_a = {}

    def read_file(self):
        mini_data = open("mini_data.txt")
        for line in mini_data:
            line = line.strip()
            line = line.split(":")
            self.q_and_a[line[0]] = line[1].strip()

    def game_play(self):
        score = 0
        questions = self.q_and_a.keys()
        shuffle(questions)
        for question in questions:
            answer = raw_input(question + ': ')
            if answer == self.q_and_a[question]:
                print 'correct'
                score += 1
                print 'score =', score
            else:
                print "Incorrect"
                print self.q_and_a[question]

        print score/ len(questions)
        print float(score)/ len(questions)










flashcard  = Flashcards()
flashcard.read_file()
print flashcard.q_and_a
flashcard.game_play()




















































































































































































