# -*- coding = utf-8 -*-
# @Time : 2022/7/6 22:14
# @Author : 计海彪
# @File : .py
# @Software : PyCharm

'''
#这是我的第一个python程序
print("hello,world") #这是注释


这是第一行注释
张文文是
剪短发i的




print("hello，python")

a=10
print("这是变量：",a)
import keyword
print(keyword.kwlist)

age = 18
print("我的年龄是：%s岁"%age)
print("我的名字是%s,我的国籍是%s"%("小张","中国"))
print ("www","baidu","com",sep=".")
print('hello',end="")
print("world",end="\t")
print("python",end="\n")
print("end")
print()
'''
'''

password = input("请输入密码")
print("您刚刚输入的密码是",password)

a = input("输入：")
print(type(a))
print('输入了一个数字：%s'%a)



a = int("123")
print(type(a))
b = a + 100
print (b)





c = int(input("输入c:"))
print("输入了一个数字：%d"%c)
'''

'''
if True :
    print("True")
else :
    print("False")
print("end")

print("1")
'''
'''
score = 77
if score >= 90:
    print("本次考试，等级为A")
elif score >= 80 and score < 90:
    print('B')
elif score >= 70 and score <80 :
    print("C")
elif score >=60 and score <70 :
#else:
    print("E")
'''
'''
x = 1
d = 1
if x == 1:
    print("nan")
    if d ==1:
        print("jieshao")
    else:
        print('geiyige')
else:
    print('nv')
'''
'''
import random
x = random.randint(0,2)
print(x)
'''
'''
import random
b = random.randint(0,2)


a = int(input('请输入"0，1，2"中一个数字'))
if a == 0:
    if b == 1:
       print('你输了')
    elif b == 2:
        print('你赢了')
    elif b ==0 :
        print('重来')
elif a == 1:
    if b == 1:
       print('重来')
    elif b == 2:
        print('输了')
    elif b ==0 :
        print('赢了')
elif a == 2 :
    if b == 1:
       print('赢了')
    elif b == 2:
        print('重来')
    elif b ==0 :
        print('输了')
else:
    print('请输入正确的数')

'''
'''
for i in range(5):
    print(i)
'''
'''
for i in range(0,10,3):
    print (i)
'''
'''
for i in range(-10,-100,-30):
    print(i)
'''

'''
name = "chengdu"
for x in name:
    print(x,end="\t")
'''
'''
a = ["aa",'bb','cc','dd']
for i in range(len(a)):
    print(i,a[i])
'''
'''
i =0
while i < 5:
    print("当前是第%d次执行循环"%(i+1))
    print("i=%d"%i)
    i +=1
'''

'''
i = 1
a =0
n = 100
while i < n:
    i += 1
    a = a + i
print("%d结果是%d"%(n,a))
'''

'''
count =0
while count <5 :
    print(count,"xiaouy==")
    count+= 1
else:
    print(count,"大于5")
'''

'''
i = 0
while i < 10:
    i += 1
    print("-"*30)
    if i ==5:
        continue #continue是结束if循环，break是结束while循环
    print(i)
'''
'''
a = 1
b = 1
sum = 0
for a in range(1,10):
    for b in range(1,10):
        sum =a * b
        print("%d * %d = %d"%(b,a,sum),end="\t")
'''
'''
a = 1
sum =0
for a in range(1,10):
    b = 1
    while b < a:
        sum = a * b
        print("%d * %d = %d"%(a,b,sum),end="\t")
        b += 1
    if b ==a:
        sum = a * b
        print("%d * %d = %d" %(a, b, sum))


word = '字符串'
sentens = "这是一个句子"
paragraph = """
       这是一个段落
       激动亢奋

print(word)
print(sentens)
print(paragraph)



my_str = "I\"'m a student"

#my_str = 'I\\m a student'

print(my_str)

'''



'''
str = "chengdu"
print(str[0:5:2])
print(str[1:6:3])
print(str[3:])
print(str[:4])

print(str + ",你好")
print(str *3)

print("hello\nchengdu")                                                                                                   #使用反斜杠，实现转义字符功能，换行

print(r"hello\nchengdu")                                                                                                  #前面加r，不转译

'''


'''
#8.列表

namelist = [] #定义一个空列表
namelist = ["小张","小王","小李"]
print(namelist[0])


testlist = [1,"测试"]

print(testlist[0])
print(testlist[1])


print(type(testlist[0]))
print(type(testlist[1]))#列表中可以存储不同类型的东西

for name in namelist:
    print(name)

print(len(namelist))

lenth = len(namelist)

i = 0
while i<lenth:
    print(namelist[i])
    i +=1

'''
'''

#增加{append，extend}
namelist = ["小张","小王","小李"]
print('------增加前，列表数据-----')
for name in namelist:
    print(name)
nametemp = input('请输入要增加的姓名')
namelist.append(nametemp)     #在末尾增加一个元素
print('------增加后，列表数据-----')
for name in namelist:
    print(name)
'''

'''
a = [1,2]
b =[3,4]

a.append(b) #将列表当作一个元素，加入到a列表中
print(a)

a.extend(b) #将列表中的每个元素，逐一追加到a中
print(a)

'''
'''
#insert
a = [0,1,2]
a.insert(1,3)  #第一个表示下标，第二个表示元素
print(a)   #指定位置追加一个元素
'''

'''
#删除

moviename = ["加勒比海盗","黑客帝国","第一滴血","第一滴血","速度与激情"]

print("-----删除前电影列表数据-----")
for name in moviename:
    print(name)

del moviename[2]#指定位置删除元素

moviename.pop() #弹出末尾最后一个元素

moviename.remove("第一滴血")#直接删除指定内容的元素(只删除重复内容的第一个元素)

print("-----删除后电影列表数据-----")
for name in moviename:
    print(name)

'''

'''
#改


namelist = ["小张","小王","小李"]
print('------修改前，列表数据-----')
for name in namelist:
    print(name)

namelist[1] = "小红" #修改指定下标内容

print('------修改后，列表数据-----')
for name in namelist:
    print(name)


'''

'''

#查【in，not in】
namelist = ["小张","小王","小李"]
findname = input("请输入需要查找的姓名")
if findname in namelist:
    print("在名单里")
else:
    print("不在")
'''
'''
a = ["a","b","c","a","b"]


print(a.index("a",1,4)) #在1-4范围内查找指定的元素，并返回指定元素的下标
print(a.index("a",1,3)) #范围区间左闭右开[1,3),找不到会报错
'''
'''
a = ["a","b","c","a","b"]
print(a.count('b')) #统计元素出现次数

'''
'''
#排序

a = [1,4,2,3]
print(a)
a.reverse()  #将列表所有元素反转

print(a)

a.sort() #升序

a.sort(reverse=True)  #降序

print(a)
'''
'''
schoolname = [[],[],[]]  #有三个元素的空列表，每个元素都是空列表

schoolname =[["北京大学","清华大学"],["南开大学","天津大学","天津师范大学"],["山东大学","中国海洋大学","潍坊医学院"]]

print(schoolname[0][0])  # 第一个是schoolname里面的元素下标，第二个是第一个元素里的第一个元素

'''
'''
import random    # 随机数生成
offices = [[],[],[]]
names = ["a","b","c","d","e","f"]
for name in names:
    index = random.randint(0,2)   # 随机数生成
    offices[index].append(name)

i = 1
for office in offices:
    print("办公室的%d人数为：%d"%(i,len(office)))
    i +=1
    for name in office:
        print("%s"%name,end="\t")
    print("\n")
    print("-"*20)
 

'''
'''
import random
offices = [[],[],[]]
teachers = ["a","b","c","d","e","f"]
for teacher in teachers:
    index = random.randint(0,2)
    offices[index].append(teacher)

i = 1
for office in offices:      #遍历
    print("办公室%d的人数为：%d"%(i,len(office)))
    print("分别为%s"%office , end="\n")
    i += 1
    print("----"*20)
'''
'''
products = [["iphone",6888],["MacPro",14800],["小米6",2499],["Coffee",31],["Book",60],["NIke",699]]

print("-"*2,end="\t")
print("商品列表",end="\t")
print("-"*2)

i = 0


for product in products:
    print(i,end="\t")
    print(product[0],end="\t")
    print(product[1])
    i += 1

carts =[[],[]]
a = 0

while a < 7:
    aaa = input("你想买什么")
    if aaa == "q":
        print(carts[0], end="\t")
        print(carts[1])
        break

    else:
        index = int(aaa)
        for i in range(0,5):
            if index == i:
                   carts[0].append(products[i][0])
                   carts[1].append(products[i][1])
a += 1

'''

#元祖
'''
tup1 = ()  #创建一个空的元祖

tup2 = (50)  #不是元组，，<class 'int'>
print(type(tup2))
tup = (50,)
print(type(tup)) #这是一个元组


tup1 = ("abc","def","2000","2020",232,222,6644)
print(tup1[0])
print(tup1[-1])
print(tup1[1:5])  #左闭右开，进行切片


#增加
tup1 = (12,34,56)
tup2 = ("abc","idnd")
tup = tup1 + tup2
print(tup)

#删除
tup1 = (12,34,56)
del tup1
print("删除后")
print(tup1)  #删除整个元组

'''
#修改
'''
tup1 = (12,34,56)
tup1[0] = 100  #报错，不能修改
'''
#查
#同list







#dict 字典  （key-value）键-值对


#字典的定义
'''
info = {"name":"吴彦祖","age":18}

'''
#字典的访问
'''
print(info["name"])
print(info["age"])

#访问了不存在的键

#print(info["gender"])   #直接访问会报错

print(info.get("gender"))  #使用get方法，没有找到对应的键，默认返回：none

print(info.get("gender","m"))   #没有找到对应的键，返回"m",如果找到了，返回原来的值


'''

#增
'''

info = {"name":"吴彦祖","age":18}

newID  = input("请输入学号")
info["id"] = newID

print(info["id"])

'''
'''
#删
#【del】
info = {"name":"吴彦祖","age":18}
print("删除前：%s"%info["name"])

del info["name"]

print("删除后：%s"%info["name"])  #删除指定键值对后，再次访问会报错

'''
'''
info = {"name":"吴彦祖","age":18}
print("删除前：%s"%info)
del info
print("删除后：%s"%info)  #报错

'''

#【clear】
'''
info = {"name":"吴彦祖","age":18}
print("清空前：%s"%info)
info.clear()
print("清空后：%s"%info)
'''
#改
'''
info = {"name":"吴彦祖","age":18}
info["age"] = 20
print(info["age"])
'''


#查（遍历）
'''
info = {"id":1,"name":"吴彦祖","age":18}
print(info.keys())     #得到的键是列表形式

print(info.values())    #得到的值是列表形式

print(info.items())     #每个键值对是元组，dict_items([('id', 1), ('name', '吴彦祖'), ('age', 18)])
'''
#遍历所有的键
'''
info = {"id":1,"name":"吴彦祖","age":18}
for key in info.keys():
    print(key)
'''
#遍历所有的值
'''
info = {"id":1,"name":"吴彦祖","age":18}
for value in info.values():
    print(value)
'''



#遍历所有的键值对
'''
info = {"id":1,"name":"吴彦祖","age":18}
for key,value in info.items():
    print("key=%s,value=%s"%(key,value))
'''


'''
mylist = ["a","b","c","d"]
for i,x in enumerate(mylist):  #使用枚举函数，同时拿到列表中的下标和元素内容
    print(i,x)
'''

#集合


'''
#函数的定义
def printinfo():
    print("--------------")
    print("人生苦短，我用python")
    print("------------------")

#函数的调用
printinfo()
'''


'''
#带参数的函数


def add2Num(a,b):
    c = a+b
    print(c)

add2Num(11,22)
'''
'''
#带返回值的函数
def add2Num(a,b):
    return a+b
result = add2Num(11,22)
print(result)            #第一种

print(add2Num(22,33))     #第二种
'''


#返回多个值的函数
'''



def divid(a,b):
    shang = a//b
    yushu = a%b
    return shang,yushu
sh,yu = divid(5,2)                                  #需要多个值来保存
print("商:%d,余数：%d"%(sh,yu))
'''

#打印横线

'''
def printOneLine():
    print("-"*30)

def PrintNumLine(num):
    i = 0
    while i < num:
        printOneLine()
        i += 1
PrintNumLine(int(input("打印几条横线")))

def hengxian(a):
    print("-"*a)
hengxian(int(input("打印几条横线")))
'''
'''
# 求三个数的和
def plus(a,b,c):
    d = a+b+c
    return d
print(plus(10,20,30))                               #打印求和结果

A=int(input("a"))
B=int(input("b"))
C=int(input("c"))
def ave(a,b,c):
    aveg = int(plus(a,b,c))/3
    print(plus(a, b, c))
    print("三个数的平均值是：%d"%(aveg))
ave(A,B,C)
'''

'''
#全局变量和局部变量

a=1000                                               #全局变量

def test1():
    a= 300    #局部变量  优先使用

    print("test1______修改前：a=%d"%a)
    a =100
    print("test1______修改后：a=%d" % a)

def test2():

    print("test2------a=%d"%a)                           #没有局部变量   默认访问全局变量
test1()
test2()


#在函数中修改

a = 1000  # 全局变量


def test1():
    global a                                            #申明全局变量在函数中的标识符
    print("test1______修改前：a=%d" % a)
    a = 100                                             #修改了全局变量
    print("test1______修改后：a=%d" % a)


def test2():
    print("test2------a=%d" % a)                   # 没有局部变量   默认访问全局变量


test1()
test2()
'''
'''
f = open("test.txt","w")          # 打开文件，w模式（写模式），如果没有创建新文件
f = open("test.txt")              # 没有w,就是r模式，如果没有文件就报错
f.close()                         #关闭文件
'''
'''
f = open("test.txt","w")
f.write("hello world,i am here")    #将字符串写入文件中
f.close()  
'''


'''
# read方法，读取指定的字符，开始时定位在头部，没执行一次向后移动一定字符数
f = open("test.txt","r")
content = f.read(5)
print(content)
content = f.read(5)              #从第一个读的末尾开始读
print(content)
f.close()
'''
'''
f = open("test.txt","r")

content = f.readlines()    #一次性读取全部文件为列表，每行一个字符串元素
print(content)

i = 1
for temp in content:
    print("%d:%s"%(i,temp ))
    i += 1

f.close()
'''
'''
f = open("test.txt","r")

content = f.readline()       #一次性读一行
print("1:%s"%content,end="")   

content = f.readline()
print("2:%s"%content)

f.close()
'''


'''
import os
os.rename("test.txt","test1.txt")    #重命名文件名


'''
''
#捕获异常
try:
    print("test1")
    f = open("123.txt","r")
    print("test2")
except IOError:
    pass
'''