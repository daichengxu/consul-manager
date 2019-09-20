# !/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Dai"
# Date: 2019/9/19

from core import views,node,service,deregister

def Run():
    node.Search_Node()
    service.Search_Service(state="critical")
    service_dict = views.Check_Service()
    for serviceid in service_dict:
        consulname = service_dict.get(serviceid)
        consulip = views.Check_NodeIP(name=consulname)
        print('consul name: %s' % consulname, 'service id: %s' % serviceid, 'consul ip:%s' % consulip)
    selector=raw_input("请确认是否清除consul注册(y/n): ")
    if selector == 'y':
        for serviceid in service_dict:
            consulname = service_dict.get(serviceid)
            consulip = views.Check_NodeIP(name=consulname)
            deregister.Deregister(NodeIP=consulip, ServiceID=serviceid)
        exit(0)
    elif selector == 'n':
        print "exit system."
        exit(0)
    else:
        print "input error,exit system."
        exit(1)

if __name__ == '__main__':
    Run()

