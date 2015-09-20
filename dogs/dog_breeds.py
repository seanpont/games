


breeds = "Affenpinscher Afghan Afghan Aidi Airedale Akbash Akita Alano Alaskan Alaskan Alpine Alpine American American American American American American American American American Anatolian Andalusian Anglo Appenzeller Ariege Ariegeois Armant Armenian Artois Australian Australian Australian Australian Australian Australian Austrian Austrian Azawakh Bakharwal Barbet Basenji Basque Basque Basset Basset Basset Basset Basset Basset Bavarian Beagle Beagle Bearded Beauceron Bedlington Belgian Belgian Belgian Belgian Bergamasco Berger Berger Berner Bernese Bichon Billy Black Black Black Black Blackmouth Bleu Bleu Bloodhound Blue Blue Blue Bluetick Boerboel Bohemian Bolognese Border Border Borzoi Bosnian Boston Bouvier Bouvier Boxer Boykin Bracco Italia"

breeds_with_attributes = []

for breed in breeds.split(' '):
    # print breed
    size = 0
    if len(breed) >= 7:
        size = 2
    elif len(breed) >= 4:
        size = 1

    sheds = len(breed) % 2 == 0

    breeds_with_attributes.append((breed, size, sheds))

for b in breeds_with_attributes:
    print b


desired_size = int(raw_input("Enter house size: 0, 1, or 2: "))
allergies = raw_input("Do you have allergies? y or n: ")
desired_shedding = True
if allergies == 'y':
    desired_shedding = False

assert type(desired_size) == int
assert type(desired_shedding) == bool

for breed in breeds_with_attributes:
    if breed[1] == desired_size and breed[2] == desired_shedding:
        print breed[0]


















