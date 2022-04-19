# -*- coding:utf-8 -*-

import pymysql.cursors
from Andrew.Common.ReadConfig import ini
from Andrew.Common.LogTool import log
from prettytable import from_db_cursor

class MysqlOperate():

    """
    数据库工具类封装
    """
    def __init__(self):

        try:
            self.conn = pymysql.connect(host = ini._get('Mysql', 'host'),
                                        user = ini._get('Mysql', 'user'),
                                        port = int(ini._get('Mysql', 'port')),
                                        password = ini._get('Mysql', 'password'),
                                        database = ini._get('Mysql', 'db_name'),
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
            return table
        except Exception as e:
            log.error("sql语句错误: {}: {}".format(e.args[0],e.args[1]))
            return None

mysql = MysqlOperate()

if __name__ == '__main__':
    sql = "SELECT ID,SUMMARY_SERIAL_NUMBER,REBATE_MODULE_NAME,SECOND_LEVEL_ENTERPRISE_NAME,SECOND_LEVEL_ENTERPRISE_CRM_CODE,AMOUNT_PAID AS 已支付金额,REMAINING_AMOUNT AS 剩余金额,OCCUPIED_AMOUNT AS 已占用金额,REBATE_IMPORT_DATE FROM rebate AS r WHERE FIRST_LEVEL_ENTERPRISE_NAME = '天津广丰大药房有限公司';"
    log.debug(f" \n {mysql.execute_sql(sql)}")
    mysql.close()