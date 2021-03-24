
import random
'''
1.由系統亂數產生 1~49 之間六個不重複的整數，請排序遞增印出
2.由系統產生7個整數數字(亂數 1 ~ 100)
  要遞增排序印出來 [....]，由使用者輸入一個值去找尋串列中的值
  用二分法顯示尋找過程
4.由使用者輸入獲利金額
  1、含10萬以內，獎金10%
  2、10萬~20萬(低於10萬獎金10%,剩餘的獎金7%)
  3、20~40萬(低10 => 10% , 10萬 => 7% ,剩:3%)
      39萬 == 10*10% + 10*7% + 19*3%
'''
# 1.
# scort = [] 
# for num in range(6) :
#    num = random.randint(1,50)
#    scort.append(num)
#    if scort.count(num)==0:
#        print(scort)
# scort.sort()
# print(scort)

# 2.
scort=[]
for num2 in range(7):
    num2 = random.randint(1,101)
    scort.append(num2) 
    
scort.sort()
print(scort)

ch=int (input('請輸入尋找的數字:'))
def binary_search(scort,ch):
    left =0
    right=len(scort)-1
    count=0
    while left <= right:
        count+=1
        mid = (left + right) // 2
        st  = (scort[mid])
        print('中間數是:',st)
        print('找:',count,'次')
        if st < ch :
            left = mid+1
        elif st > ch:
            right = mid-1
        else:
            return mid
    return -1
        
index = binary_search(scort, ch)
if index >= 0 :
    print('找到數值索引:'+str(index))
else:
    print('找不到數值')    


