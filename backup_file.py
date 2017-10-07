# -*- coding=utf-8 -*-

import subprocess

if __name__ == '__main__':
    db_names = [
        'house'
    ]
    for db in db_names:
        cmd = 'cd {dir};tar czvf {file_name}.tar {dir_name};'.format(dir = '/var/lib/mysql', file_name = '%s_%s' % (
            db, 'backup'), dir_name = db)
        subprocess.Popen(cmd, shell = True)
