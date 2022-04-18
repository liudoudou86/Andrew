# -*- coding:utf-8 -*-

import pymysql
from Andrew.Common.ReadConfig import ini

class MysqlOperate():

    """
    数据库工具类封装
    """
    def __init__(self):
        self.conn = pymysql.connect(host = ini._get('Mysql', 'host'),
                                    user = ini._get('Mysql', 'user'),
                                    port = int(ini._get('Mysql', 'port')),
                                    password = ini._get('Mysql', 'password'),
                                    database = ini._get('Mysql', 'db_name'),
                                    charset ='UTF8')
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

    def execute_sql(self, sql, one=True):
        """
        执行sql语句
        """
        self.cursor.execute(sql)
        if one:
            return self.cursor.fetchone()
        else:
            return self.cursor.fetchall()

    def close(self):
        """
        关闭数据库连接
        """
        self.cursor.close()
        self.conn.close()

mysql = MysqlOperate()

if __name__ == '__main__':
    sql = "select * from rebate"
    print(mysql.execute_sql(sql, one=True))
    mysql.close()