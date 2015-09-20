


from dog_breed_downloader import DogBreedDownloader, DogBreed

breeds = DogBreedDownloader().download_breeds()

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


















