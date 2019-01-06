import sqlite3

import os


class MySql():
    def __init__(self):
        self.logo_pic='logo'
        self.origin_pic='origin'

        self.conn = sqlite3.connect("sqlite.db")
        self.cur=self.conn.cursor()
        query = """create table IF NOT EXISTS Setting(
            name VARCHAR(20) unique,
            value text,
            date TimeStamp NOT NULL DEFAULT CURRENT_TIMESTAMP   
        );"""
        self.conn.execute(query)
        query2 = """create table IF NOT EXISTS history(
            id int not null primary key,
            path text ,
            folder text,
            file text,
            date TimeStamp NOT NULL DEFAULT CURRENT_TIMESTAMP   
        );"""
        self.conn.execute(query2)
        # self.insert((self.logo_pic,'C:\\'))
        # self.insert(('proportion','500:500'))
        # self.insert(('logo', ''))
        # self.insert(('save', 'D:\\test'))
        # self.insert(('origin',r'C:\Users\frank\Pictures\Camera Roll'))
    def check_exits(self,value):
        '''

        :param value:name,value
        :return:
        '''
        query="select * from Setting where name='%s'"%value[0]
        self.cur.execute(query)
        res=self.cur.fetchall()
        if res:
            return res
        else:
            return 0

    def insert(self,value):
        if value!=() and value:
            if self.check_exits(value):
                query = "update Setting set value='%s' where name='%s'" % (value[1], value[0])
            else:
                query = "insert into Setting(name,value)values('%s','%s')" % value
            self.cur.execute(query)
            self.conn.commit()
    def insert_path(self,value):
        '''
        data(name,value)
        '''
        if value and value[1]!='':
            if value[0]=='url':
                if self.check_exits(value):
                    query="update Setting set value='%s' where name='%s'"%(value[1],value[0])
                else:
                    query="insert into Setting(name,value)values('%s','%s')"%value
            else:
                if value[1][-1]=='/' or value[1][-1]=='\\' :

                    if self.check_exits(value):
                        query="update Setting set value='%s' where name='%s'"%(value[1],value[0])
                    else:
                        query="insert into Setting(name,value)values('%s','%s')"%value
                else:
                    if '/' in value[1]:
                        address=value[1]+'/'
                    else:
                        address = value[1] + '\\'
                    if self.check_exits(value):
                        query="update Setting set value='%s' where name='%s'"%(address,value[0])
                    else:
                        query="insert into Setting(name,value)values('%s','%s')"%(value[0],address)
                print(query)
            self.cur.execute(query)
            self.conn.commit()
    def select_logo_path(self):
        query="select name,value from Setting where name='%s'"%self.logo_pic
        self.cur.execute(query)
        res =self.cur.fetchall()
        print(res)
        if res:
            return res
        else:
            return 0
    def select(self):
        query="select * from Setting"
        self.cur.execute(query)
        res=self.cur.fetchall()
        if res:
            return res
        else:
            return 0
    # def write_to_txt(self):

    def save_path(self):
        query="select * from Setting where name='save'"
        self.cur.execute(query)
        res=self.cur.fetchall()
        if res:
            return res
        else:
            return 0
    def origin_path(self):
        query="select * from Setting where name='origin'"
        self.cur.execute(query)
        res=self.cur.fetchall()
        if res:
            return res
        else:
            return 0

    def select_setting(self,name):
        query="select name,value from setting where name='%s'"%name
        self.cur.execute(query)
        res=self.cur.fetchall()
        if res:
            return res
        else:
            return 0