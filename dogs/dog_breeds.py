from dog_breed_downloader import DogBreedDownloader, DogBreed

breeds = DogBreedDownloader().download_breeds()

print '\n'.join(map(str, breeds[:100])), '\n...'

print len(breeds)


















