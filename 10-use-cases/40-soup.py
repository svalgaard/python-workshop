#! /usr/bin/env python3
#
# Requires requests, beautifulsoup4 and lxml
#

import bs4
import urllib
import os

NEXT_URL = "https://download.nextcloud.com/desktop/releases/Windows/"
DESTINATION = "/tmp/"


def find_urls():
    # Fetch data from URL
    data = urllib.request.urlopen(NEXT_URL).read().decode('utf-8')
    soup = bs4.BeautifulSoup(data, 'lxml')

    # Find relevant links
    urls = []
    for a in soup.find_all('a'):
        href = urllib.parse.urljoin(NEXT_URL, a['href'])
        if href.endswith('.exe'):
            urls.append(href)
    return urls


def download(url):
    fn = os.path.split(url)[-1]
    lfn = os.path.join(DESTINATION, fn)

    if not os.path.isfile(lfn):
        print(f'Downloading {url}')
        data = urllib.request.urlopen(url).read()
        open(lfn, 'wb').write(data)


def main():
    if not os.path.isdir(DESTINATION):
        os.makedirs(DESTINATION)

    for url in find_urls():
        download(url)


if __name__ == '__main__':
    main()
