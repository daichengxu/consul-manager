# !/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Dai"
# Date: 2019/9/19

from config import configer
from core import views
from urllib2 import URLError
import urllib2,json

def Search_Node():
    """
    获取consul节点信息
    GET http://nodeip:8500/v1/agent/members
    传参给 Save_Node(data)
    :return:
    """
    url = views.Def_url(type="node")
    try:
        response=urllib2.urlopen(url,timeout=5)
        httpcode = response.getcode()
        httpcode = "info: " + url + " " + str(httpcode)
        views.Run_log(data=httpcode)
        httpcontent=response.read()
        Save_Node(data=httpcontent)
        # print httpcode
    except URLError as e:
        message = "error: " + str(url) + " " + str(e.reason)
        views.Run_log(data=message)
        print  "error: " + str(url) + " " + str(e.reason)
        exit(1)

def Save_Node(data=None):
    """
    存储节点信息到 ./data/node.json
    :param data: Search_Node(data=res2)返回的节点数据
    :return:
    """
    datapath=configer.Data_DIR+'/node.json'
    f = open(datapath, "r+")
    f.truncate()
    dict_json = json.loads(data)
    for data in dict_json:
        with open(datapath, 'a+') as f:
            f.write(json.dumps(data) + '\n')
