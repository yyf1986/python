#!/usr/local/bin/python2.7
#coding=utf-8
'''
Created on 2014-4-11

@author: YAO
'''

import paramiko
class SSH(object):
    def __init__(self,ip,user,password="",timeout=5):
        self.ip = ip
        self.user = user
        self.password = password
        self.timeout = timeout
    def run(self,cmd):
        import socket
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((self.ip,22))
            s.close()
            restlt = "connect"
        except Exception,e:
            restlt = "N-connect"
        if restlt == "connect":
            try:
                #paramiko.util.log_to_file('paramiko.log') 
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(self.ip,22,self.user, self.password,timeout=self.timeout)
                stdin, stdout, stderr  = ssh.exec_command(cmd)
                stdin = "y"
                out = stdout.readlines()
                if len(str(out)) == 2:
                    out = "NULL"
                else:
                    out = out
            except Exception,e:
                if str(e) == "Authentication failed.":
                    out = "A-ERROR"
                else:
                    out = "INFO-ERROR"
            finally:
                ssh.close()
        else:
            out = "C-ERROR"
        return out
    def getfile(self,remotefile,localfile):
        import socket
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((self.ip,22))
            s.close()
            restlt = "connect"
        except Exception,e:
            restlt = "N-connect"
        if restlt == "connect":
            try:
                t = paramiko.Transport((self.ip,22))
                t.connect(username = self.user, password = self.password)
                sftp = paramiko.SFTPClient.from_transport(t)
                sftp.get(remotefile,localfile)
                out = "SUCESS"
            except Exception,e:
                if str(e) == "Authentication failed.":
                    out = "A-ERROR"
                else:
                    out = "INFO-ERROR"
            finally:
                t.close()
        else:
            out = "C-ERROR"
        return out
    def scpfile(self,localfile,remotefile):
        import socket
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((self.ip,22))
            s.close()
            restlt = "connect"
        except Exception,e:
            restlt = "N-connect"
        if restlt == "connect":
            try:
                t = paramiko.Transport((self.ip,22))
                t.connect(username = self.user, password = self.password)
                sftp = paramiko.SFTPClient.from_transport(t)
                sftp.put(localfile,remotefile)
                out = "SUCESS"
            except Exception,e:
                if str(e) == "Authentication failed.":
                    out = "A-ERROR"
                else:
                    out = "INFO-ERROR"
            finally:
                t.close()
        else:
            out = "C-ERROR"
        return out
