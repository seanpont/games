


def suicide_circle(people, skip):
    l = []
    index = 0
    p_l = range(1, people+1)
    while len(p_l) > 1:
        index += skip
        index = (index) % len(p_l)
        l.append(p_l.pop(index))
        print index
    return l


print suicide_circle(200, 7)








































