#!/usr/bin/python3
"""
Write a Python script that takes in a URL and sends a request
to the URL and displays variable X-Request-Id in the response header
"""
import sys
import requests

if __name__ == '__main__':
    reqs = requests.get(sys.argv[1])
    print(reqs.headers.get("X-Request-Id"))
