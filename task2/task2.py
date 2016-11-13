#!/usr/bin/env python
#_*_coding:utf-8_*_
#authory:luca


import yaml
f = open('memu.yaml')
dataMap = yaml.load(f)
f.close()
#print(dataMap)

while True:

    for index1,memu in  enumerate(dataMap.keys()):
        print(index1,memu)
    choice1 =  input("Please input the 1 memu Num, input Q exit:")
    if choice1 == 'Q':
        break
    if choice1.isdigit():
        choice1 = int(choice1)
        if choice1 < len(dataMap):
            onekey = list(dataMap.keys())[choice1]
            #print(onekey)
            #print("2")
            while True:
                for index2, submemu in enumerate(dataMap[onekey]):
                    print(index2,submemu)
                choice2 = input("Please input the 2 submemu Num, input B back:")
                if choice2 == 'B':
                    break
                if choice2.isdigit():
                    choice2 = int(choice2)
                    if choice2 < len(dataMap[onekey]):
                        twokey =list(dataMap[onekey].keys())[choice2]
                        print(twokey)

                        while True:
                            for index3, sonmemu in enumerate(dataMap[onekey][twokey]):
                                print(index3,sonmemu)
                            choice3 = input("Please input the 3 sonmemu Num, input B back:")
                            if choice3 == 'B':
                                break
                            if choice3.isdigit():
                                choice3 = int(choice3)
                                #print(choice3)
                                #print(len(dataMap[onekey][twokey]))
                                #print(dataMap[onekey][twokey])
                                if choice3 < len(dataMap[onekey][twokey]):
                                    threekey = list(dataMap[onekey][twokey].keys())[choice3]
                                    #print(threekey)
                                    while True:
                                       for index4,atom in enumerate(dataMap[onekey][twokey][threekey]):
                                            print(index4,atom)
                                       choice4 = input("Please input  B back:")
                                       if choice4 == 'B':
                                           break









