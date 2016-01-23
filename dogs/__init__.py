from dog_breed_downloader import DogBreedsDownloader
from collections import namedtuple

DogBreed = namedtuple('DogBreed', 'name origin group image_url')


def download_breeds():
    """
    :return: [DogBreed]
    """
    return DogBreedsDownloader().download_breeds()
