#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Dai"
# Date: 2019/9/19

from config import configer
from core import views
from urllib2 import URLError
import urllib2,json

def Search_Service(state="critical"):
    """
    查询异常服务 "critical"
    GET http://nodeip:8500/v1/health/state/critical
    :param state:  "any", "unknown", "passing", "warning", or "critical"
    :return:
    """
    url = views.Def_url(type="service", state=state)
    try:
        response=urllib2.urlopen(url=url,timeout=5)
        httpcode = response.getcode()
        httpcode = "info: " + url + " " + str(httpcode)
        views.Run_log(data=httpcode)
        httpcontent=response.read()
        Save_Service(data=httpcontent)
        # print httpcode
    except URLError as e:
        message = "error: " + str(url) + " " + str(e.reason)
        views.Run_log(data=message)
        print  "error: " + str(url) + " " + str(e.reason)
        exit(1)

def Save_Service(data=None):
    """
    存储节点信息到 ./data/data.json
    :param data: Search_Service(data=res2)返回的节点数据
    :return:
    """
    datapath=configer.Data_DIR+'/data.json'
    f = open(datapath, "r+")
    f.truncate()
    dict_json = json.loads(data)
    for data in dict_json:
        with open(datapath, 'a+') as f:
            f.write(json.dumps(data) + '\n')
