#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/8 22:12          
# @Author  : Za_Nks                   
# @File    : application.py               
from app.url import url

import tornado.web
import os

setting = dict(
    template_path=os.path.join(os.path.dirname(__file__), "template"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    )


application = tornado.web.Application(
    handlers=url,
    **setting
)

