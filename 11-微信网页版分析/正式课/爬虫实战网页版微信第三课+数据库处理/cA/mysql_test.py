#!/usr/bin/env python
# -*- coding: utf-8 -*-
from cA.mysql_handle import Mysql

__author__ = 'Terry'

def insert(sql, params=None):
    try:
        mysql = Mysql()
        ret = mysql.insertOne(sql, params)
    finally:
        mysql.dispose()

    return ret

def insert_many(sql, params=None):
    try:
        mysql = Mysql()
        ret = mysql.insertMany(sql, params)
    finally:
        mysql.dispose()

    return ret

def delete(sql, params=None):
    try:
        mysql = Mysql()
        ret = mysql.delete(sql, params)
    finally:
        mysql.dispose()

    return ret

def update(sql, params=None):
    try:
        mysql = Mysql()
        ret = mysql.update(sql, params)
    finally:
        mysql.dispose()

    return ret

def get_one(sql, params=None):
    try:
        mysql = Mysql()
        ret = mysql.getOne(sql, params)
    finally:
        mysql.dispose()

    return ret

def get_many(sql, params=None, num=None):
    try:
        mysql = Mysql()
        ret = mysql.getMany(sql, num, params)
    finally:
        mysql.dispose()

    return ret

def get_all(sql, params=None):
    try:
        mysql = Mysql()
        ret = mysql.getAll(sql, params)
    finally:
        mysql.dispose()

    return ret

if __name__ == '__main__':
    # 增， 不能插入自增的id字段
    # ret = insert('INSERT INTO tb_test(title, content) '
    #              'VALUES(%s, %s);', ('测试标题', '测试内容'))
    # ret = insert('INSERT INTO tb_test(title, content) '
    #              'VALUES("测试标题拼写", "测试内容拼写");')
    # ret = insert_many('INSERT INTO tb_test(title, content) '
    #                   'VALUES(%s, %s);', [('测试标题22', '测试内容22'), ('测试标题23', '测试内容23')])
    # print(ret)

    # 删
    # ret = delete('DELETE FROM tb_test where title="测试标题"')
    # ret = delete('DELETE FROM tb_test where title=%s', ("测试标题"))
    # print(ret)

    # 改
    # ret = update("UPDATE tb_test SET title='测试修改标题10' where title='测试标题10';")
    # ret = update("UPDATE tb_test SET title=%s where title=%s;", ('测试标题10', '测试标题22'))
    # print(ret)

    #查
    # ret = get_one('select * from tb_test order by id')
    ret = get_many('select * from tb_test', 2)
    # ret = get_many('select * from tb_test where title=%s', params='测试标题10')
    # ret = get_all('select * from tb_test')
    print(ret)

    print('over')