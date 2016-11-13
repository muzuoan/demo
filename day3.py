#!/usr/bin/env python
#_*_coding:utf-8_*_
#print "消费升级驱动中国经济"

#user_input1 = input("input your name:")
#print ("user input msg:", user_input1 )
#name="daidai"
#name=input("input your girl frend name:")
#print(name)

import os
cmd=os.popen('df -h').read()
print(cmd)


import sys
print(sys.path)
