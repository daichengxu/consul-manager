# !/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Dai"
# Date: 2019/9/19

from core import views
from urllib2 import URLError
import urllib2

def Deregister(NodeIP=None,ServiceID=None):
    """
    执行consul service去注册
    PUT http://NodeIP:8500/v1/agent/service/deregister/ServiceID
    :param NodeIP: 接收consul ip地址
    :param ServiceID: 接收serviceID
    :return:
    """
    url="http://"+NodeIP+":8500/v1/agent/service/deregister/"+ServiceID
    try:
        request = urllib2.Request(url)
        request.get_method = lambda: 'PUT'
        response = urllib2.urlopen(request,timeout=5)
        httpcode = response.getcode()
        httpcode = "info: " + url + " " + str(httpcode)
        views.Run_log(data=httpcode)
        # print httpcode
    except URLError as e:
        message = "error: " + str(url) + " " + str(e.reason)
        views.Run_log(data=message)
        print  "error: " + str(url) + " " + str(e.reason)
        exit(1)
