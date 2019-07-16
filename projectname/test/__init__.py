#!/bin/python
# -*- coding:utf-8 -*-
'''
@author: xc
@time: 2019-07-16
'''

import logging
from logging.handlers import TimedRotatingFileHandler

LOG_LEVEL = logging.INFO
LOG_FILE_NAME = 'xc_test'

logger = logging.getLogger()
logger.setLevel(LOG_LEVEL)
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
BASIC_FORMAT = '%(asctime)s\tFile \"%(filename)s\",line %(lineno)s\t%(levelname)s: %(message)s'
formatter = logging.Formatter(BASIC_FORMAT, DATE_FORMAT)

#创建StreamHandler对象
log_stream_handler = logging.StreamHandler()
log_stream_handler.setFormatter(formatter)
logger.addHandler(log_stream_handler)

#创建TimedRotatingFileHandler对象
log_file_handler = TimedRotatingFileHandler(filename='../logs/%s.log'%(LOG_FILE_NAME), when="midnight", interval=1, backupCount=15)
log_file_handler.setFormatter(formatter)
logger.addHandler(log_file_handler)

#logger.info('testlog')