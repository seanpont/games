# def josephus(p,s):
#   people = range(1,p+1)
#   index = 0
#   pop = []
#   while len(people) > 0:
#     index = (index + s) %len(people)
#     pop.append(people.pop(index))
#   return pop
#
# print josephus(26, 17)


#_________________________________________________________________

def hot_cold():
  import random
  password = 'pouki'
  r = random.randint(0,100)
  if raw_input('what is your name?: ') == 'Alexia':
    if password == raw_input('password: '):
      print r
  user_guess = raw_input("guess a number: ")
  user_guess = int(user_guess)
  if user_guess == r:
    print "you won!!!"
  else:
    while user_guess != r:
      user_guess_2 = raw_input('guess again: ')
      user_guess_2 = int(user_guess_2)
      if user_guess_2 == r:

        print "you won"
        return
      elif abs(r - user_guess) < abs(r - user_guess_2):
        print 'colder'
      else:
        print 'warmer'
      print r
      user_guess = user_guess_2

hot_cold()
































