#!/usr/bin/env python
#_*_coding:utf-8_*_
#authory:luca
import yaml
import os


def login(username,password):
    '''
    user login function
    :return:
    '''
    f = open("userdb",'r')
    for line in f:
        line_list =line.strip().split("|")
        if line_list[0] == username and line_list[1] == password:
            salary = line_list[2]
            return  (username,salary,True)

    return  (username,salar,False)
#
def  recharge(salary):
    money= input("please input how much recharge:")

    if money.isdigit():
        salary = salary + int(money)
        return salary


def shop(username,balance):
    welcome_msg = 'Welcome to 711 Shoping mall'
    print(welcome_msg)


    f = open('productdb')
    dataMap = yaml.load(f)
    f.close()
    #print(dataMap)
    shop_car=[]


    while True:
        for index,category in enumerate(dataMap.keys()):
            print(index,category)
        choice=input("Please input the 1 memu Num, input Q exit:")
        if choice == "Q":
                break
        if  choice.isdigit():
            choice=int(choice)
            if choice <len(dataMap):
                key=list(dataMap.keys())[choice]
                while True:
                    for index,product in  enumerate(dataMap[key]):
                        print(index,product)
                    product_ID = input("[C=check;B=back] what do you want buy?")
                    if product_ID == "B":
                        break
                    if product_ID.isdigit():
                        product_ID=int(product_ID)
                        if product_ID < len(dataMap[key]):
                            product_name=list(dataMap[key].keys())[product_ID]
                            product_info=dataMap[key][product_name]
                            price_info=dataMap[key][product_name][0]
                            sum_info=dataMap[key][product_name][1]
                            #print(sum_info)
                            product_price=int(price_info.split(":")[1])
                            product_sum=sum_info.split(":")[1]
                            if product_price < balance:
                                shop_car.append((product_name,product_price))
                                balance = balance - product_price
                                print("add [%s] into shop car ,you current balance is \033[31;1m[%s]\033[0m" % (product_name, balance))
                            else:
                                print("your balance is \033[31;1m[%s]\033[0m, can't afford this" % balance)
                            #print(product_name,product_price,product_sum)
                        else:
                            print("your choice is not exist")
                    if product_ID == "C":
                        print("purchased product as follow")
                        f = open(username, 'a')
                        for item in shop_car:
                            f.newlines
                            f.write(item[0]+"\n")
                            print(item)
                        print("END".center(60, '-'))
                        print("your balance is [%s]" % balance)
                        f.close()
                        break

    print("welcome next time")



def main():
    exit_flag = False
    user = input("please input your name:")
    pwd =input("please input your password:")
    login_info = login(user,pwd)

    if  login_info[2]:

        mesg = '''
            Your name is %s balance is %s.
            you can recharge or shoping:
            1:Enter recharge
            2:Enter shop
        ''' %(login_info[0],login_info[1])
        print (mesg)

        if os.path.exists("./"+user):
            f=open(user)
            last_shop=f.readlines()
            print("your shop info last time is %s."%last_shop)

        balance = int(login_info[1])
        while exit_flag is not True:
            choice = input("Q=[quit];please input your choice:")
            if choice == "Q":
                break
            if choice.isdigit():
                choice=int(choice)
                if choice == 1 :
                    balance =recharge(balance)
                    #print("Your balance is %s."%balance)
                if choice == 2 :
                    shop(login_info[0],balance)
                    exit_flag = True



    else:
        print("login failed")

main()






























