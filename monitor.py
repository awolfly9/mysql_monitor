# -*- coding=utf-8 -*-

import yaml
import json
import config
from send_email import send_email
from hammer.sqlhelper import SqlHelper


def get_info(db, res):
    table = res.get('TABLE_NAME')
    update_time = res.get('UPDATE_TIME')
    rows = res.get('TABLE_ROWS')

    info = '数据库:{db} 表名:{table} 更新时间:{update} 数据行数:{rows}\n'. \
        format(db = db, table = table, update = update_time, rows = rows)

    return info


if __name__ == '__main__':
    with open('config.yaml', 'r') as stream:
        datas = yaml.load(stream)

    sql = SqlHelper(**config.db_config)
    full_info = '\n'

    db_datas = datas.get('db')
    for db, tables in db_datas.items():
        command = '''SELECT * FROM `information_schema`.TABLES;'''
        cmd = ''
        if len(tables) > 0:
            cmd += ' and '
            for i, table in enumerate(tables):
                if i > 0:
                    cmd += ' or '

                cmd += 'table_name=\'{}\''.format(table)

        command = '''SELECT * FROM `information_schema`.TABLES WHERE table_schema = \'{db}\' {table}'''. \
            format(db = db, table = cmd)

        print('command:%s' % command)

        result = sql.query(command)
        for res in result:
            full_info += get_info(db, res)

    print('full_info:%s' % full_info)
    send_email(datas.get('email'), 'mysql 监控日志', full_info)
