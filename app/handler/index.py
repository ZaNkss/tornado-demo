#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/8 22:15          
# @Author  : Za_Nks                   
# @File    : index.py
import logging

import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        logging.getLogger('mylogger').info("hello")
        self.write("hello")
