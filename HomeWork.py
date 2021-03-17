# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 12:08:17 2021

@author: user
"""
# import random
'''
1. 印"*"
*****
****
***
**
*
**
***
****
*****

2.求使用這輸入一個範圍的整數
    求4的倍數有哪些?
    求哪些是質數?(只可被1跟自己整除)
    
3.min=1
  max=100
  
  沒猜中顯示目前猜數範圍
  如果猜錯達5次 break
  
'''
#1.印"*"
# for i in range(5,0,-1):
#     #print('i=',i)
#     for a in range(0,i):
#         print('*',end='')
#     print() # 斷行
# for i in range(2,6):
#     for a in range(0,i):
#         print('*',end='')
#     print() # 斷行
    
# print("程式執行完畢")
# print("*"*20)

#2.#求4的倍數有哪些?
# star = int(input("初始值:"))
# end  = int(input("終結值:"))

# for i in range(star,end):
#     if i%4 == 0:
#         print(i,"是4的倍數")
# prime_num =[]
# for i in range(star+1,end):
#     for j in range(1,i):
#         if i %j == 0 and j !=1:
#             break
#         elif j == i - 1 :
#             prime_num.append(i)
# print(prime_num)

# print("*"*20)

#3.# 電腦猜數(顯示目前猜數範圍)
# min=1
# max=100
# ans = random.randint(min,max)
# guess=0
# total=0
# while ans != guess:
#     guess = int (input('輸入1~100之間的整數猜數:'))
#     total+=1
#     if total>=5:
#         print("答錯超過次數")
#         break
#     if guess>ans :
#         print('猜小一點')
#         print(min,"~",guess)
#     elif guess<ans :
#         print('猜大一點')
#         print(guess,"~",max)
    
    

