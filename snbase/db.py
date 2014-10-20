#!/usr/bin/python
#-*- coding: utf-8 -*-
'''
Created on 2014-2-25

@author: 11113072
'''
import MySQLdb
import sys
import snlog

class Db():
    def __init__(self):
        try:
            self.conn = MySQLdb.connect(host='192.168.242.11',user='root',passwd='itsmsitdb',db='snpub',charset="utf8")
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
    def insert_Event(self,manager,task_desc,msg):
        ''' 插入事件，执行成功返回I-SUCESS，失败返回I-FAIL '''
        sql= "insert into sn_event(event_source,event_type,event_octime,event_firstdealuser,event_introduction,event_describe,event_intime,event_commituser,event_status) values(%s,%s,now(),%s,%s,%s,now(),%s,%s)"
        param = ("系统巡检","应用系统",manager,task_desc,msg,"系统巡检","已提交")
        try:
            self.cursor.execute(sql,param)
            self.conn.commit()
            result = "I-SUCESS"
        except Exception:
            result = "I-FAIL"
        return result
    def select_Manager(self,vm_system):
        ''' 根据自动巡检任务，查找系统管理员，执行成功返回list，失败返回S-ERROR，或者数据部存在返回N-DATA '''
        sql = "select system_manager1 from sn_system where system_cname ='"+vm_system+"'"
        try:
            n = self.cursor.execute(sql)
            if n != 0:
                data = self.cursor.fetchall()
            else:
                data = "N-DATA"
        except Exception:
            data = "S-ERROR"
        return data
    def close(self):
        ''' 关闭连接 '''
        self.cursor.close()
        self.conn.close()
