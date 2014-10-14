#!/usr/bin/python2.6
#-*- coding: utf-8 -*-
'''
Created on 2014-2-25

@author: 11113072

'''

import socket
import httplib

def checkport(ip,port):
    ''' 检查端口，超时时间2s，通过返回值来判断端口是否开启  o是正常，N-connect端口不能连接'''
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((ip,port))
        s.close()
        restlt = "o"
    except Exception:
        restlt = "N-connect"
    return restlt
def getcode(ip,port,url,timeout=5):
    ''' 抓取url状态码，返回结果为字符串类型，异常为N-connect '''
    try:
        conns = httplib.HTTPConnection(ip,port,True,timeout)
        if not url.startswith('/'):
            url="/"+url
        conns.request("GET",url)
        response = conns.getresponse()
        code = response.status
        result = code
    except Exception:
        result = "N-connect"
    finally:
        conns.close()
    return result
