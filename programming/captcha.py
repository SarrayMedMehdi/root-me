import re
import subprocess
import sys
import string
import httplib, urllib
import base64
from PIL import Image

 

def go(passwd):
    params = urllib.urlencode({'cametu': passwd})
    headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = httplib.HTTPConnection("challenge01.root-me.org")
    conn.request("POST", "/programmation/ch8/", params, headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    print data
    return data

def clean_img():
    img = Image.open("im.png") # delete all the noise ;)
    width, height = img.size
    pix = img.load()
    for i in range(width):
        for j in range(height):
       	    if pix[i, j] == (0, 0, 0):
                pix[i, j] = (255, 255, 255)
    img.save("imclean.png")
	

def get_the_image():
    basedata = go('blabla')
    img = re.match(r".*base64,(.*?)\".*", basedata)
    img = img.group(1)
    with open("im.png","wb") as f:
        f.write(base64.b64decode(img)) 
	


def using_gocr():
    p = str(subprocess.check_output('gocr imclean.png -u ',shell=True)).strip()
    print p
    sys.stdout.flush()
    return p
	

def main():
    get_the_image()
    clean_img()
    go(using_gocr())
	
if  __name__ =='__main__':
    main()


