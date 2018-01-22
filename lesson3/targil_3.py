import random
x = random.randint (1, 1001)
y = str(x)+".png"
print(y)
import urllib.request
url = 'http://i1-news.softpedia-static.com/images/news2/Picture-of-the-Day-Real-Life-Simba-and-Mufasa-Caught-on-Camera-in-Tanzania-392687-2.jpg'
filename = y
urllib.request.urlretrieve(url, y)

#urllib.request.urlretrieve(url, filename=None, reporthook=None, data=None)¶
