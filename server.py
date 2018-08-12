#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/8 22:11          
# @Author  : Za_Nks                   
# @File    : server.py
import logging.config
import tornado.ioloop
import tornado.options
import tornado.httpserver
import yaml

from app.application import application
from tornado.options import define, options
from app.util.log_formatter import LogFormatter

define("port", default=8888, help="run on th given port", type=int)


def main():
    tornado.options.parse_command_line()
    # 格式化日志输出
    [i.setFormatter(LogFormatter()) for i in logging.getLogger().handlers]
    # 从配置文件引入自定义的logger
    with open('app/config/logger.yml', 'r') as f_conf:
        dict_conf = yaml.load(f_conf)
    logging.config.dictConfig(dict_conf)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    print('Development server is running at http://127.0.0.1:%s/' % options.port)
    print('Quit the server with Control-C')
    tornado.ioloop.IOLoop.instance().start()


if __name__=="__main__":
    main()