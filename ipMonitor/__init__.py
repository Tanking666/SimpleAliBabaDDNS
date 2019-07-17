#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-26 15:36
# @Author  : Tanking
# @File    : __init__.py
import re
import urllib.request


def getIp():
    url = r'http://txt.go.sohu.com/ip/soip'
    r = urllib.request.urlopen(url).read()
    ip = re.findall(r'\d+.\d+.\d+.\d+', str(r))
    return ip[0]
