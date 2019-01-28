#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/12/31 09:18
@File    : test_parseurl.py
@Author  : frank.chang@shoufuyou.com



<scheme>://<netloc>/<path>;<params>?<query>#<fragment>
"""

from urllib.parse import urlparse



from urllib3.util.url import  parse_url



url = "https://frank@localhost:80/accounts.google.com/b/0/AddMailService?baz=1&num=10#part1"


parsed = parse_url(url)


print(parsed)

print(parsed.scheme,parsed.netloc,parsed.path,parsed.query,parsed.fragment)

print('frank')
if __name__ == '__main__':
    pass
    
