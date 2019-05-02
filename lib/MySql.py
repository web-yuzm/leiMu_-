import sqlite3

import os


class MySql():
    def __init__(self):
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
