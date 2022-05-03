# downloads all of the images from https://xkcd.com/

import bs4, requests, os
from pathlib import PurePath

os.makedirs('xkcd images', exist_ok=True) #create the xkcd images folder

for i in range(1,2600):
    response = requests.get('https://xkcd.com/' + str(i))
    try:
        response.raise_for_status ()
    except Exception as exc: 
        print ('invalid site:  ' + str (response))
    soup = bs4.BeautifulSoup(response.content, 'lxml')
    image_list = soup.select("#comic > img")
    for i in image_list:
        lnk = i['src']
        with  open(PurePath('xkcd images').joinpath(PurePath(lnk).name), 'wb') as f:
            f.write (requests.get('https:' + str(lnk)).content)
            print ('downloading image  %s ...' % PurePath(lnk).name)
