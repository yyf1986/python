#!/usr/bin/python2.6
#-*- coding: utf-8 -*-
'''
Created on 2014-4-18

@author: 11113072
'''
import redis
class Snredis(object):
    def __init__(self,ip,port,password="",db=0):
        self.r = redis.Redis(host=ip,port=port,db=db,password=password)
    def info(self):
        try:
            self.info = self.r.info()
            return self.info
        except redis.exceptions.ConnectionError:
            return "port can not connect"
        except redis.exceptions.ResponseError:
            return "require password"
    def used_mem(self):
        used_memory = str(self.info["used_memory"])
        return used_memory
    def max_mem(self):
        try:
            maxmemory = str(self.r.suningconfig_get("maxmemory")[1])
        except redis.exceptions.ResponseError:
            maxmemory = str(self.r.config_get("maxmemory")["maxmemory"])
        return maxmemory
    def snf_flag(self):
        snf_flag = str(self.r.get('__SNF__REDIS__DISABLED__SIGN__'))
        return snf_flag
    def max_clients(self):
        try:
            maxclients = str(self.r.suningconfig_get("maxclients")[1])
        except redis.exceptions.ResponseError:
            maxclients = str(self.r.config_get("maxclients")["maxclients"])
        return maxclients
    def append_status(self):
        try:
            append = str(self.r.suningconfig_get("appendonly")[1])
        except redis.exceptions.ResponseError:
            append = str(self.r.config_get("appendonly")["appendonly"])
        return append
    def connected_client(self):
        connected_clients = str(self.info["connected_clients"])
        return connected_clients
