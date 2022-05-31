# -*- coding:utf-8 -*-

import pymysql.cursors
from Andrew.Common.LogUtil import log
from Andrew.Common.ReadConfig import ini
from prettytable import from_db_cursor

# 读取数据库配置参数
host = ini._get('Mysql', 'host')
user = ini._get('Mysql', 'user')
port = int(ini._get('Mysql', 'port'))
password = ini._get('Mysql', 'password')
database = ini._get('Mysql', 'db_name')

class MysqlOperate():

    """
    读取数据库工具类封装
    """
    def __init__(self):

        try:
            self.conn = pymysql.connect(host = host,
                                        user = user,
                                        port = port,
                                        password = password,
                                        database = database,
                                        charset ='UTF8')
            self.cursor = self.conn.cursor()
        except Exception as e:
            log.error("数据库连接失败: {}: {}".format(e.args[0],e.args[1]))
            exit()
    
    def close(self):
        """
        关闭数据库连接
        """
        self.cursor.close()
        self.conn.close()

    def execute_sql(self, sql):
        """
        执行sql语句
        """
        try:
            self.cursor.execute(sql)
            table = from_db_cursor(self.cursor)
            self.conn.commit()
            return table
        except Exception as e:
            log.error("sql语句错误: {}: {}".format(e.args[0],e.args[1]))

mysql = MysqlOperate()

if __name__ == '__main__':
    sql = "select * from ch_channel"
    log.debug(f" \n {mysql.execute_sql(sql)}")
    mysql.close()