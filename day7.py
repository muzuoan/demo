#!/usr/bin/env python
#_*_coding:utf-8_*_
#authory:luca


salary = input("input you salary:")
if salary.isdigit():
    salary = int(salary)
else:
    exit("Invaild data type...")




product_list = [
    ('IPhone7',6000),
    ('ipod',1000),
    ('oneplus',2000),
    ('bag',100),
    ('Bike',800),
    ('Cloth',80)
]

shop_car = []

exit_flag = False
while exit_flag is not True:

    for item in enumerate(product_list):
        index=item[0]
        product_item=item[1][0]
        product_price=item[1][0]
        print(index,".", product_item,product_price)
    user_choice = input("[q=quit;c=check] what do you want buy?")
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if user_choice < len(product_list):
            p_item = product_list[user_choice]
            if p_item[1] <= salary:
                shop_car.append(p_item)
                salary = salary - p_item[1]
                print("add [%s] into shop car ,you current balance is \033[31;1m[%s]\033[0m" %(p_item,salary))
            else:
                print("your balance is \033[31;1m[%s]\033[0m, can't afford this" %salary)
                #break
        else:
            print("your choice is not exist")
    else:
        if user_choice == 'q' or user_choice == 'quit':
            print("purchased product as follow")
            for item in shop_car:
                print(item)
            print("END".center(60,'-'))
            print("your balance is [%s]" %salary )
            print("welcome next time")
            exit_flag = True
        elif user_choice == 'c' or user_choice == 'check':
            print("purchased product as follow")
            for item in shop_car:
                print(item)
            print("END".center(60, '-'))
            print("your balance is [%s]" % salary)

