#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-26 15:24
# @Author  : Tanking
# @File    : __init__.py
import json
import urllib
import urllib.request
import ipMonitor

WEBHOOK = "https://oapi.dingtalk.com/robot/send?access_token=YourDingDingRobotToken"
HEADER = {'Content-Type': 'application/json'}


def say(text):
    data = {
        "msgtype": "text",
        "text": {
            "content": text
        },
        "at": {
            "atMobiles": [],

        },
        "isAtAll": False
    }
    data = json.dumps(data)
    data = bytes(data, "utf8")
    send_req(data)


def send_req(data):
    req = urllib.request.Request(WEBHOOK, data, HEADER)
    res = urllib.request.urlopen(req).read()
    print(res)



