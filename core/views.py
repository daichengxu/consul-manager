#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Dai"
# Date: 2019/9/19

from config import configer
import time,ast

def Run_log(data=None):
    """
    运行日志
    :param data: 日志信息
    :return:
    """
    runtime = 'Date: %s' % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    datapath=configer.Data_DIR+"/run.log"
    try:
        with open(datapath, 'a+') as f:
            f.write(runtime + '\n')
        with open(datapath, 'a+') as f:
            f.write(data + '\n')
    except Exception as e:
        print e

def Def_url(type=None,state=None):
    """
    定义url地址
    http://nodeip:8500/v1/agent/members
    http://nodeip:8500/v1/health/state/state
    :param type: "node","service","deregister"
    :param state: "any","unknown","passing","warning","critical"
    :return: url 地址
    """
    nodeip = configer.Node_IP
    if type == "node":
        url_path="http://"+nodeip+":8500/v1/agent/members"
    elif type == "service":
        url_path="http://"+nodeip+":8500/v1/health/state/"+str(state)
    else:
        url_path=None
    return url_path

def Check_Service():
    """
    获取ServiceID,Node
    :return: dict
    """
    datapath=configer.Data_DIR+'/data.json'
    service_dict={}
    with open(datapath, 'r') as f:
        service_dict_list=f.readlines()
    for data in service_dict_list:
        data=ast.literal_eval(data)
        service_id=data["ServiceID"]
        service_node=data["Node"]
        service_dict[service_id]=service_node
    return service_dict

def Check_NodeIP(name=None):
    """
    获取consul ip地址
    :param name: 传入ServiceID
    :return: 返回consul ip地址
    """
    datapath=configer.Data_DIR+'/node.json'
    with open(datapath, 'r') as f:
        node_dict_list=f.readlines()
    for data in node_dict_list:
        data=ast.literal_eval(data)
        node_name=data["Name"]
        node_ip=data["Addr"]
        if node_name == name:
            return node_ip
