#!/usr/bin/python3
"""script that takes in a URL and an email address, sends a POST request"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {"email": email}
    r = requests.post(url, params=data)
    print("Your email is: {}".format(r.text))
