#Case1_collatz
def collatz(number):
    if number%2==0:
        print(number//2)
        n=number//2
    else:
        print(3*number+1)
        n=3*number+1
    return n#定义collatz函数
print("Please enter a number")
EnteredNumber=int(input())
while EnteredNumber==1:
    print("The number you entered first can not 1")
    print("Please entered the number again")
    EnteredNumber=int(input())
    continue
while EnteredNumber!=1:
    EnteredNumber=collatz(EnteredNumber)
    continue
print("Well,the number you entered has been calculated to 1 finally")

#Case2_逗号代码
def Confun(list):
    n=len(list)
    i=0
    x='answer is '
    while i<n-1:
        x=x+str(list[i])+', '
        i=i+1
    if i==n-1:
        x=x+"and"+str(list[i])
    return x
spam=['apples','bananas','tofu','cats']
print(Confun(spam))

#Case3_字符网格
 grid = [ ['.', '.', '.', '.', '.','.'],
          ['.', '0', '0', '.', '.','.'],
          ['0', '0', '0', '0', '.','.'],
          ['0', '0', '0', '0', '0','.'],
          ['.', '0', '0', '0', '0','0'],
          ['0', '0', '0', '0', '0','.'],
          ['0', '0', '0', '0', '.','.'],
          ['.', '0', '0', '.', '.','.'],
          ['.', '.', '.', '.', '.','.']]
 c=[]
 c=copy.deepcopy(grid)
 print(c)
 gridLen=len(grid)
 cyctime=len(grid[0])
 print(gridLen)
 print(cyctime) 
# i=0(Can be deleted cause defautly equal 0)
# j=0(Can be deleted cause defautly equal 0)
 for j in range(cyctime):
     if j < cyctime :
         for i in range(gridLen):
             if i < gridLen :
                 print(c[i][j],end=' ')
                 i=i+1
     print('\n')
     j=j+1

#打印字符数量
import pprint
message='it was a bright cold day in APril, and the clocks were striking.'
count={}
for character in message:
    count.setdefault(character,0)
    count[character]=count[character]+1
pprint.pprint(count)

#井字棋盘
theboard={'top-L':' ','top-M':' ','top-R':' ',
'mid-L':' ','mid-M':' ','mid-R':' ',
'bot-L':' ','bot-M':' ','bot-R':' '}
def printboard(board):
    print(board['top-L']+'|'+board['top-M']+'|'+board['top-R'])
    print('-+_+_')
    print(board['mid-L']+'|'+board['mid-M']+'|'+board['mid-R'])
    print('-+_+_')
    print(board['bot-L']+'|'+board['bot-M']+'|'+board['bot-R'])
turn='x'
for i in range(9):
    printboard(theboard)
    print('Turn for '+turn+' .Move on which space')
    print('Please enter the location on the board')
    move=input()
    theboard[move]=turn
    if turn=='x':
        turn='o'
    else:
        turn='x'
printboard(theboard)

#嵌套字典和列表
allguest={
'Alice':{'apples':5,'pretzels':12,'bananas':7},
'Bob':{'bananas':7,'pineapples':8},
'Ann':{'pie':88,'drink':22}
}
def totalbrought(guest,item):
    numBrought=0
    for k,v in guest.items():
        numBrought=numBrought+v.get(item,0)
        print(k)
        print(numBrought)
    return numBrought
print('Number of the items')
print('apples'+str(totalbrought(allguest,'apples')))
print('pretzels'+str(totalbrought(allguest,'pretzels')))
print('bananas'+str(totalbrought(allguest,'bananas')))
print('pineapples'+str(totalbrought(allguest,'pineapples')))
print('pie'+str(totalbrought(allguest,'pie')))
print('drink'+str(totalbrought(allguest,'drink')))

#列表到字典并统计显示
def add_inventory(inventory, added_items):
    for k in added_items:
        inventory.setdefault(k, 0)
        inventory[k] = inventory[k]+1
    return inventory

def display_inventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v)+' '+k)
        item_total += v
    print('Total number of items:'+str(item_total))

inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_inventory(inv, dragon_loot)
display_inventory(inv)

#计算字符串中的字母数量，并且做清晰的换行打印
import pprint
message='it was a bright cold day in APril, and the clocks were striking.'
count={}
for character in message:
    count.setdefault(character,0)
    count[character]=count[character]+1
    print(character)
    print(count[character])
print(pprint.pformat(count))

#copy_password
#!/usr/bin/env python3
#coding:utf-8
PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
'luggage': '12345'}
import pyperclip,sys
if len(sys.argv)<2:
    print('Usage:python[account]-copy account password')
    sys.exit()
account=sys.argv[1]
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(' Password for ' + account + ' copied to clipboard.')
    print(PASSWORDS[account])
else:
    print(' There is no account named ' + account)

#批量改变剪贴板内容格式
#!/usr/bin/env python3
#encoding:utf-8
import pyperclip
text=pyperclip.paste()
#Separatelinesandaddstars.
lines=text.split('\n')
for i in range(len(lines)):#loopthroughallindexesfor"lines"list
    lines[i]='* '+lines[i]#addstartoeachstringin"lines"list
text='\n'.join(lines)
m=pyperclip.copy(text)
print(m)

#表格对齐打印
import copy
def count_width(the_list):
    new_list = copy.deepcopy(the_list)
    col_widths = [0]*len(the_list)
    i = 0
    while i < len(new_list):
        new_list[i].sort(key=lambda x: len(x), reverse=True)
        col_widths[i] = new_list[i][0]
        i = i+1
    return col_widths
def list_ljust(the_list):
    widths = count_width(the_list)
    for j in range(len(the_list[0])):
        for i in range(len(the_list)):
            print(the_list[i][j].ljust(len(widths[i])), end=' ')
        print('\r')
table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]
list_ljust(table_data)

#强口令检测
import re
password1=str(input())
def CheckStrongPassword(password):
    if len(password)<8:
        print('This is not a good password')
        return False
    else:
        chpw1=re.compile(r'[a-z]+').search(password)
        chpw2=re.compile(r'[A-Z]+').search(password)
        chpw3=re.compile(r'[0-9]+').search(password)
        if chpw1==None or chpw2==None or chpw3==None:
            print('wrong')
            return False
        else:
            print('true')
            return True
print(CheckStrongPassword(password1))

#strip()的正则表达式版本
import re
print('Please enter the text')
text=str(input())
print('Plesase enter the parameter')
parameter=str(input())#输入参数
def ReStrip(text,parameter):
    if parameter=='':
        textregex=re.compile(r'^\s*|\s*$')
        print(textregex.sub('', text))
    else:
        textregex=re.compile(parameter)
        print(textregex.sub('',text))#定义函数
ReStrip(text, parameter)#运行结果

#随机出非固定题目及选项的试卷
import random
capitals={'Alabama':'Montgomery','Alaska':'Juneau',
'Arizona':'Phoenix','California':'Sacramento'}

for quiznum in range(2):

    quizfile=open('capitalsquiz%s.txt'%(quiznum+1),'w')
    answerkeyfile=open('capitalsquiz_answers%s.txt'%(quiznum+1),'w')

    quizfile.write('Name:\n\nData:\n\nPeriod:\n\n')
    quizfile.write((''*20)+'State Capitals Quiz (Form%s)'%(quiznum+1))
    quizfile.write('\n\n')

    states=list(capitals.keys())
    random.shuffle(states)

    for questionnum in range(2):
        correctanswer=capitals[states[questionnum]]
        wronganswers=list(capitals.values())
        del wronganswers[wronganswers.index(correctanswer)]
        wronganswers=random.sample(wronganswers,3)
        answeroptions=wronganswers+[correctanswer]
        random.shuffle(answeroptions)
        quizfile.write('%s.what is the capital of %s\n'%(questionnum+1,states[questionnum]))
        for i in range (4):
            abcd=['A','B','C','D']
            quizfile.write(abcd[i]+'.%s\n'%answeroptions[i])
        quizfile.write('\n')
        answerkeyfile.write('%s.%s\n'%(questionnum+1,'ABCD'[
            answeroptions.index(correctanswer)]))
    quizfile.close()
    answerkeyfile.close()

#多重剪贴板
#!/usr/bin/env python3
import sys,pyperclip,shelve
mcbshelf=shelve.open('mcb')
if len(sys.argv)==3 and sys.argv[1].lower()=='save':
    mcbshelf[sys.argv[2]]=pyperclip.paste()
elif len(sys.argv)==2:
    if sys.argv[1].lower()=='list':
        pyperclip.copy(str(list(mcbshelf.keys())))
    elif sys.argv[1] in mcbshelf:
         pyperclip.copy(mcbshelf[sys.argv[1]])
mcbshelf.close()

#登录系统查询成绩并修改密码
import random
import shelve
#将数据存入文件db中
with shelve.open("db") as f:
    #scores是一个列表，通过get方法获取score的值：若score中有值，则scores=score；如果没有，则scores=[]
    scores=f.get("score",[])
    #accounts是一个字典，通过get方法获取accounts的值：若account中有值，则accounts=account；如果没有，则accounts={"admin":"12345"} 
    accounts=f.get("account",{"admin":"12345"})
    for i in range(3):
        id=input("用户名:")
        password=input("密码:")
        if id in accounts and accounts[id]==password:
            print('成绩表：',scores)
            name=input("name:")        #向列表中添加学生姓名
            cj=random.randint(50,100)  #向列表中添加学生成绩，范围为（50,100）
            scores.append([name,cj])
            print('成绩表：',scores)
            npass=input("新密码:")
            f["score"]=scores
            f["account"]={"admin":npass}
            break
        else:
            print("用户名或密码错误！")
    else:
        print("三次机会已用完，再见！")
#通过字典的形式获取文件db中的数据
print('---------------------------')
with shelve.open('db') as f:
    for k,v in f.items():
        print(k,':',v)
       
#疯狂填词
#疯狂填词
import re
originalfile = open('file.text', 'w')
originalfile.write('The ADJECTIVE pand walked to the NOUN and VERB.\nA nearby NOUN was unaffected by these event.')
originalfile.close()
originalfile = open('file.text', 'r')
longstr = originalfile.read()
print('原文本如下:\n'+str(longstr))
print('现在需要您将以下改词进行替换')
#将原始文本写入指定文件，并且读出该文件内的相关内容
textregex = re.compile(r'ADJECTIVE|NOUN|VERB')

mmo = textregex.findall(longstr)

for i in range(len(textregex.findall(longstr))):

    subregex = re.compile(mmo[i])

    mo = subregex.search(longstr)

    print('Please input the '+mo.group())

    subtext = str(input())

    longstr = subregex.sub(subtext, longstr,count=1)

print('替换后的最终结果为:'+longstr+'\n现将其写入另一个全新文件')
newfile = open('newfile.text', 'w')
newfile.write(longstr)
newfile.close()
