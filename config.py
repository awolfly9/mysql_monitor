# coding=utf-8

db_config = {
    'pool_name': 'monitor',
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'database': 'mysql',
    'pool_resize_boundary': 2,
    'enable_auto_resize': True,
    'max_pool_size': 1
}

email_type = 'qq'

# gmail
if email_type == 'gmail':
    self_email = 'awolfly9@gmail.com'
    self_password = '123456'
elif email_type == 'qq':  # qq
    self_email = '1412238085@qq.com'
    self_password = '123456'
