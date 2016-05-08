

def gg():
    import random
    random_int = random.randint(0, 100)
    user_input = raw_input("Guess a number between 1 and 100:")
    number = int(user_input)
    if number == random_int:
        print "Congratulations you won"
    else:
        while number != random_int:
            user_input2 = raw_input("Guess again: ")
            user_input2 = int(user_input2)
            if user_input2 == random_int:
                print "Congratulations you won"
            elif abs(random_int - number) < abs(random_int - user_input2):
                print "Colder"
            else:
                print "Warmer"
            number = user_input2




gg()







































