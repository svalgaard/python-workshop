#! /usr/bin/env python3
#
# Requires mechanicalsoup
# https://mechanicalsoup.readthedocs.io/en/stable/tutorial.html
#

import mechanicalsoup
import sys


def main():
    global response, text
    query = sys.argv[1]

    browser = mechanicalsoup.StatefulBrowser()

    # Go to main Google page
    browser.open("https://google.dk/")
    form = browser.select_form()
    form['q'] = query
    response = browser.submit_selected()

    # Print cleaned up text
    text = response.soup.body.text
    print(response.soup.body.text)


if __name__ == '__main__':
    main()
