#!/usr/bin/python3
"""
- Write a Python script that sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""
from sys import argv
from urllib import error, request

if __name__ == "__main__":
    url = argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as e:
        print("Error code:", e.code)
