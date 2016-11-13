#!/usr/bin/env python
#_*_coding:utf-8_*_
#authory:luca


import getpass

exit_flag = False
have_flag = False

while exit_flag is not True:
    file = open('userinfo.txt', 'r+')
    db_info = file.readlines()
    db_dic = dict()
    username = input("Please input your account: ")
    # passwd=getpass.getpass("Please input your password:") #pycharm不支持隐藏回显
    if len(username) == 0 :continue
    passwd = input("Please input your password:")
    print("Your account is %s and your password is %s" % (username, passwd))

    index = 0
    for temp in db_info:
        userinfo=temp.strip().split(":")
        if username == userinfo[0]:
            have_flag = True
            if userinfo[2] == "locked":
                print("The account is locked")
                exit_flag = True
            else:
                error_count = int(userinfo[3])
                if passwd == userinfo[1]:
                    print("hi,%s .welcome login. ".center(60, "-") % username)
                    exit_flag = True
                    break
                else:
                    error_count = error_count +1
                    print("The password is wrong,plese try again.")
                    if int(error_count) <3:
                       #file.write(temp.replace(userinfo[3],str(error_count)))
                        db_info[index]=temp.replace(userinfo[3],str(error_count))
                        file = open('userinfo.txt', 'w+')
                        file.writelines(db_info)
                        file.flush()
                    else:
                        #file.write(temp.replace("normal","locked"))
                        db_info[index] = temp.replace(userinfo[3], str(error_count))
                        db_info[index] = db_info[index].replace(userinfo[2], "locked")
                        file = open('userinfo.txt', 'w+')
                        file.writelines(db_info)
                        file.flush()
                        print("input error password count  greater than 3, The account is locked")
                        exit_flag = True

        index =index + 1


    if have_flag is   False:
            print("The account is not exist.")

