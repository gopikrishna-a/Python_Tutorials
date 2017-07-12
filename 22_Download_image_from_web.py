import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1,1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)


download_web_image("https://plus.google.com/u/0/photos/101400045329191782744/albums/profile/6431112530976097746")
    
