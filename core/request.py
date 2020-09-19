#!/usr/bin/env python3
import requests

def get():
    try:
        r = requests.get('http://google.com')
        return f'[!] {r.status_code}'
    except:
        return 'Connection Error'
