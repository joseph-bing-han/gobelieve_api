# -*- coding: utf-8 -*-

DEBUG=True

REDIS_HOST="192.168.33.10"
REDIS_PORT=6379
REDIS_DB=1
REDIS_PASSWORD="123456"

MYSQL_HOST = "192.168.33.10"
MYSQL_PORT = 3306
MYSQL_AUTOCOMMIT = True
MYSQL_CHARSET = 'utf8'
MYSQL_USER = "im"
MYSQL_PASSWD = "123456"
MYSQL_DATABASE = "gobelieve"

MYSQL = (MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWD, MYSQL_DATABASE, MYSQL_AUTOCOMMIT, MYSQL_CHARSET)

FS_HOST="192.168.33.10"
FS_PORT=8083

IM_RPC_URL = "http://192.168.33.10:6666"


#支持外部群组id
EXTERNAL_GROUP_ID=True
