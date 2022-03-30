#displays most popular pics on Imgur for the command line input 

import requests, bs4, webbrowser, sys
print('Searching...')
res = requests.get('https://imgur.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'lxml')
linkElems = soup.select('.image-list-link')


numOpen = min(5,len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://imgur.com' + linkElems[i].get('href')
    print ('Opening', urlToOpen)
    webbrowser.open(urlToOpen)
