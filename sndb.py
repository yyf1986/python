#!/usr/bin/python
#-*- coding: utf-8 -*-
'''
Created on 2014-2-25

@author: YAO
'''
import MySQLdb
import sys
import snlog

class Db():
    def __init__(self):
        try:
            self.conn = MySQLdb.connect(host='192.168.242.10',user='autopatrol',passwd='autopatrol',db='snpub',charset="utf8")
            self.cursor = self.conn.cursor()
        except Exception, e:
            loger = snlog.Log("db")
            loger.set_Name("dberrorinfo")
            loger.set_Level("error")
            loger.add_Msg(e)
            sys.exit()
            
    def selectInfo(self,sql):
        ''' 查询的条件直接带进sql语句，作为参数传递，执行成功返回list，失败返回S-ERROR，或者数据部存在返回N-DATA '''
        try:
            n = self.cursor.execute(sql)
            if n != 0:
                data = self.cursor.fetchall()
            else:
                data = "N-DATA"
        except Exception:
            data = "S-ERROR"
        return data
        
    def selectInfoWithArgs(self,sql,param):
        ''' 采用sql加param方式进行参数传递，执行成功返回list，失败返回S-ERROR，或者数据部存在返回N-DATA '''
        try:
            n = self.cursor.execute(sql,param)
            if n != 0:
                data = self.cursor.fetchall()
            else:
                data = "N-DATA"
        except Exception:
            data = "S-ERROR"
        return data
        
    def insertInfoWithArgs(self,sql,param):
        ''' 采用sql加param方式进行参数传递，执行成功返回I-SUCESS，失败返回I-FAIL '''
        try:
            self.cursor.execute(sql,param)
            self.conn.commit()
            result = "I-SUCESS"
        except Exception:
            result = "I-FAIL"
        return result
        
    def insertInfo(self,sql):
        ''' 插入的值直接带进sql语句，作为参数传递，执行成功返回I-SUCESS，失败返回I-FAIL '''
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            result = "I-SUCESS"
        except Exception:
            result = "I-FAIL"
        return result

    def close(self):
        ''' 关闭连接 '''
        self.cursor.close()
        self.conn.close()
