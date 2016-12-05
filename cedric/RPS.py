import random

class RPS:
    def __init__(self):
        self.moves
        self.play

def search_history ():
    a = ['a','e','f','a', 'h', 'c',]
    if len(a) < 3:
        return random.choice('rps')
    else:
        last1 = a[-1]
    count = {'r' : 0, 'p' : 0, 's' : 0}
    for i in range(len(a)-1):
        if a[i] == last1:
            count[a[i+1]] += 1
    return count

print search_history()







































































