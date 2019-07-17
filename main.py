#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-07-26 15:24
# @Author  : Tanking666
# @File    : main.py

'''
初学PY编写项目
部分参考下面网站
https://blog.csdn.net/mgsky1/article/details/80466840
'''

import sys
import time

import ipMonitor
import ddrobot
import alibabaDDNS
import os
import configparser

PATH = sys.path[0]
DDNS = 0
IP = "0.0.0.0"
DD_RP = 0
CHECKTIME = 3600
config_path = PATH + "\\robot.ini"


def load_config():
    if os.path.isfile(config_path):
        conf = configparser.ConfigParser()
        conf.read(config_path, encoding="utf-8")
        globals()["DDNS"] = conf.get("robot", "ddns")
        globals()["IP"] = conf.get("robot", "ip")
        globals()["DD_RP"] = conf.get("robot", "dingdingRP")
        globals()["CHECKTIME"] = int(conf.get("robot", "CHECKTIME"))
    else:
        create_config_file(config_path)


def create_config_file(config_path):
    f = open(config_path, "w", encoding="utf-8")
    f.write("[robot]"
            "\ndingdingRP=1"
            "\nDDNS=1"
            "\nCHECKTIME=3600"
            "\nip=0.0.0.0")
    f.close()


def save_config():
    conf = configparser.ConfigParser()
    conf.read(config_path, encoding="utf-8")
    conf.set("robot", "ip", IP)
    conf.write(open(config_path, "r+", encoding="utf-8"))


def ip_change_pro():
    if DD_RP == "1":
        ddrobot.say(IP)
    if DDNS == "1":
        alibabaDDNS.DDNS(IP)


while True:
    try:
        load_config()
    except BaseException:
        print("加载失误")
        os.system("pause")
    else:
        print("加载成功")
    realIp = ipMonitor.getIp()
    if realIp != IP:
        print("IP发生变更")
        print(IP)
        IP = realIp
        save_config()
        ip_change_pro()
    time.sleep(CHECKTIME)
