from dog_breed_downloader import DogBreedDownloader, DogBreed

breeds = DogBreedDownloader().download_breeds()

print '\n'.join(map(str, breeds[:10])), '\n...'


















