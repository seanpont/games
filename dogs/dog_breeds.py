import BaseHTTPServer
import SimpleHTTPServer
import SocketServer
import time
from dog_breed_downloader import DogBreedsDownloader

start = time.time()
breeds = DogBreedsDownloader().download_breeds()
duration = time.time() - start
print "Downloaded %d breeds in %s seconds" % (len(breeds), duration)
for breed in breeds[0:10]:
    print breed

class DogBreedRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    pass


def run(server_class=BaseHTTPServer.HTTPServer,
        handler_class=DogBreedRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


run()














