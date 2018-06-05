# -*- coding: utf-8 -*-


# # with open('pi_digits.txt') as file_object:
# #     contents=file_object.read()
# #     print(contents)
# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())


#
# file_name='pi_digits.txt'
# with open(file_name) as file_object:
#     for line in file_object:
#         print(line.rstrip())


#
# file_name='pi_digits.txt'
# with open(file_name) as file_object:
#     lines=file_object.readlines()
# for line in lines:
#     print(line.rstrip())



# file_name='pi_digits.txt'
# with open(file_name) as file_object:
#     lines=file_object.readlines()
# pi_string=''
# for line in lines:
#     pi_string+=line.strip()
# print(pi_string)
# print(len(pi_string))


# 10.1练习
# filename='learning_python.txt'
# with open(filename) as file_object:
#     contect=file_object.read()
#     print(contect.rstrip())


# filename='learning_python.txt'
# with open(filename) as file_object:
#     lines=file_object.readlines()
#     for line in lines:
#         print(line.rstrip())

#
# filename='learning_python.txt'
# with open(filename) as file_object:
#     lines=file_object.readlines()
#     plays=[]
#     for line in lines:
#         plays.append(line)
# for play in plays:
#     print(play.strip())





# filename='learning_python.txt'
# with open(filename) as file_object:
#     lines=file_object.readlines()
#     messages=[]
#     for line in lines:
#         messages.append(line)
# for massage in messages:
#     print(massage.replace('python','c').strip())
#     #print(massage.strip())







# 10.2
#  filename='guest.txt'
# name=input("输入姓名")
# with open(filename,'w') as file_object:
#     file_object.write(name)




# flag=1
# while(flag):
#     name=input("输入姓名")
#
#     if name!="ppp":
#         print("Hello " + name)
#         filename = 'guest_book.txt'
#         with open(filename, 'a') as file_object:
#             file_object.write(name + "\n")
#     else:
#         flag = 0
#
#
# flag=1
# while(flag):
#     answer=input("为什么喜欢python?\n")
#     if answer !='':
#         filename = 'answer.txt'
#         with open(filename, 'a', encoding="utf8") as file_object:
#             file_object.write(answer + "\n")
#     else:
#         flag=0





# 10.3
# num1 = input("please input a number1\n")
# num2 = input("please input a number2\n")
# try:
#     a=int(num1)
#     b=int(num2)
# except ValueError:
#     print("输入有问题")
# else:
#     print(int(a)+int(b))



# while(True):
#     num1 = input("please input a number1\n")
#     if num1=='':
#         break
#     num2 = input("please input a number2\n")
#     if num2=='':
#         break
#     try:
#         a = int(num1)
#         b = int(num2)
#     except ValueError:
#         # print("输入有问题")
#         pass
#     else:
#         print(int(a) + int(b))




# filenames=['cats.txt','dogs.txt']
# for filename in filenames:
#     try:
#         with open(filename) as file_object:
#             contents=file_object.read()
#     except FileNotFoundError:
#             # print("输入有问题")
#                 pass
#     else:
#         print(contents)



# line="Row,row,row your boat"
# print(line.count('row'))
# print(line.lower().count('row'))



# 10.4书上代码
# import json
# number=[2,3,5,7,11,13]
# filename='number.json'
# with open(filename,'w') as f_obj:
#     json.dump(number,f_obj)


# import json
# filename='number.json'
# with open(filename) as f_obj:
#     number=json.load(f_obj)
# print(number)


# import json
# usename=input("输入姓名：\n")
# filename="name.json"
# with open(filename,'w')as f_obj:
#     json.dump(usename,f_obj)
#     print("welcome back"+usename)

#
# import  json
# filename="name.json"
# with open(filename)as f_obj:
#     usename=json.load(f_obj)
#     print("welcome back "+usename)


# import  json#等效于前两个
# filename='name1.json'
# try:
#     with open(filename) as f_obj:
#         usename = json.load(f_obj)
# except FileNotFoundError:
#     usename = input("输入姓名：\n")
#     with open(filename, 'w')as f_obj:
#         json.dump(usename, f_obj)
#         print("welcome back" + usename)
# else:
#     print("welcome back "+usename)


#10.4练习
# import  json
# # num=input("输入一个喜欢的数字：\n")
# # filename='num.json'
# # with open(filename,'w') as f_obj:
# #     json.dump(num,f_obj)
#
# filename='num.json'
# with open(filename) as f_obj:
#     num=json.load(f_obj)
# print(num)



import  json
filename='num1.json'
try:
    with open(filename) as f_obj:
        num=json.load(f_obj)
        print(num)
except FileNotFoundError:
        num = input("输入一个喜欢的数字：\n")
        with open(filename,'w') as f_obj:
            json.dump(num,f_obj)

