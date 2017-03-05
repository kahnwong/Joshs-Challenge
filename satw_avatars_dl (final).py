from requests import session
from bs4 import BeautifulSoup
from urlparse import urlparse
import requests

payload = {
'view': 'login',
'username': '',
'password': '',
'login': 'Login',
'name': '',
}

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

with session() as c:
    c.post('https://satwcomic.com/login', data=payload)
    response = c.get('https://satwcomic.com/changeavatar', headers=headers)
    # print(response.headers) # display headers
    # print(response.text) # display HTML content

soup = BeautifulSoup(response.text,'html5lib')

for scrape in soup.find_all("div", class_='formato'):
	avatars = [x.get("src").encode('ascii') for x in scrape.find_all('img')] # all avatars & convert to ascii


"""Download avatars"""

for avatar in avatars[:1]:

    parsed = urlparse(avatar)
    filename = parsed.path.split('/')[-1]

    image_link = requests.get(avatar)
    # image_link = requests('GET', avatar)

    with open(filename, 'wb') as img_obj:
    	img_obj.write(image_link.content)

    print("Download " + filename + " completed!")
