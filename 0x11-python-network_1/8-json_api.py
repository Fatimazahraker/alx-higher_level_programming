#!/usr/bin/python3
"""script that takes in a URL and an email address, sends a POST request"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    if (r.status_code >= 400):
        print(f"Error code: {res.status_code}")
        exit()
    print(r.text)
