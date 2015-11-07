import SimpleHTTPServer
import SocketServer
import time
from dog_breed_downloader import DogBreedDownloader

start = time.time()
breeds = DogBreedDownloader().download_breeds()
duration = time.time() - start
print "Downloaded %d breeds in %s seconds" % (len(breeds), duration)
for breed in breeds[0:10]:
    print breed


# PORT = 8000
#
# Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
#
# httpd = SocketServer.TCPServer(("", PORT), Handler)
#
# print "serving at port", PORT
# httpd.serve_forever()


















