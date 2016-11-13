class Dog:
  def __init__(self, name, size, coat, space):
    self.name = name
    self.size = size
    self.coat = coat
    self.space = space

  def __repr__(self):
    return self.name

class Filter:
  def __init__(self, size, coat, space):
    self.size = size
    self.coat = coat
    self.space = space

  def matches(self, dog):
    return ((not self.size or dog.size in self.size) and
            (not self.coat or dog.coat in self.coat) and
            (not self.space or dog.space in self.space))


dog1 = Dog('Cedric', 'big', 'furry', 'lots')
dog2 = Dog('Tashi', 'small', 'fluffy', 'small')
dog3 = Dog('Gordon', 'medium', 'fluffy', 'medium')


DOGS = [dog1, dog2, dog3]
FILTER = Filter(['small', 'medium'], [], ['small'])
filtered = []
for dog in DOGS:
  if FILTER.matches(dog):
    filtered.append(dog)

print filtered




