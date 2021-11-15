#collatz
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

#逗号代码
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

#字符网格
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

#datachange
#!usr/bin/env python3
import re, os, shutil

datapattern=re.compile(r"""^(.*?)((0|1)?\d)-((0|1|2|3)?\d)-((19|20)?\d\d)(.*?)$""")

for amerfilename in os.listdir('/users/yangmingfan/py2'):
    mo=datapattern.search(amerfilename)
    
    if mo==None:
        continue
    beforepart=mo.group(1)
    monthpart=mo.group(2)
    daypart=mo.group(4)
    yearpart=mo.group(6)
    afterpart=mo.group(8)
    #注意搜索分组序号规则
    eurofilename=beforepart+daypart+'-'+monthpart+'-'+yearpart+afterpart
    absworkingdir=os.path.abspath('/users/yangmingfan/py2')
    amerfilename=os.path.join(absworkingdir,amerfilename)
    eurofilename=os.path.join(absworkingdir,eurofilename)

    print('Renaming "%s" to "%s"' %(amerfilename,eurofilename))
    
    shutil.move(amerfilename,eurofilename)

#文件归档为Zip
#！/usr/bin/env python3
import zipfile, os
def backuptozip(folder):
    folder=os.path.abspath(folder)
    number=1
    while True:
        zipfilename=os.path.basename(folder)+'_'+str(number)+'.zip'
        if os.path.exists(zipfilename)==False:
            break
        number=number+1
    print('Creating %s...'%(zipfilename))
    backupzip=zipfile.ZipFile(zipfilename,'w')
    for foldername, subfolder, filenames in os.walk(folder):
        print('Adding files in %s... now'%(foldername))
        backupzip.write(foldername)
        for filename in filenames:
            newBase=os.path.basename(folder)+'_'
            if filename.startswith(newBase) and filename.endwith('.zip'):
                continue
        backupzip.write(os.path.join(foldername,filename))
    backupzip.close()
    print('done')
#backuptozip('/users/yangmingfan/...')

#选择性复制
#!/usr/bin/env python3
import os, shutil
def copyselection(folder):
    for foldername, subfolder, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith('.pdf'):
                print(filename)
                shutil.copy(os.path.join(foldername,filename),'/Users/yangmingfan/copyfolder')
copyselection('/Users/yangmingfan/Secondary_Construction')
#copyselection('/Users/yangmingfan/PhotoMemory')

#选择性删除大文件
#!/usr/bin/env python3
import os, shutil, send2trash
def deletebigfile(folder):
    for foldername, subfolder, filenames in os.walk(folder):
        for filename in filenames:
            filesizepath=os.path.join(foldername,filename)
            if os.path.getsize(filesizepath) > 800:
                print(filename)
                send2trash.send2trash(filesizepath)
deletebigfile('/Users/yangmingfan/Py2')

#消除缺失的编号
import os, shutil, re
path=input('input the path')
prename=input('input the prename')
nameregex1=re.compile(r'%s\d\d\d.*'%prename)
nameregex2=re.compile(r'\d\d\d')
L=[]
for files in os.listdir(path):
    if os.path.isfile(os.path.join(path,files)) and nameregex1.search(files) is not None:
        L.append(files)
        L.sort()
print(L)
for i in range(len(L)):
    if i==0:
        continue
    if int(nameregex2.search(L[i]).group())-int(nameregex2.search(L[i-1]).group()) > 1:
        number=int(nameregex2.search(L[i-1]).group())+1
        exname=os.path.splitext(os.path.join(path,L[i]))[1]
        filename=r'%s%03d%s'%(prename,number,exname)
        shutil.move(os.path.join(path,L[i]),os.path.join(path,filename))
        L[i]=filename
print(L)

# raise Exception('This is the error message')
def boxprint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <=2:
        raise Exception('Width must be greater than 2.')
    if height <=2:
        raise Exception('Height must be greater than 2.')
    print(symbol*width)
    for i in range(height-2):
        print(symbol+(' '*(width-2))+symbol)
    print(symbol*width)

for sym, w, h in (('*',4,4),('O',20,5),('x',1,3),('ZZ',3,3)):
    try:
        boxprint(sym,w,h)
    except Exception as err:
        print('An exception happened:'+str(err))

#write errorlog
import traceback
try:
    raise Exception('This is the error message.')
except: 
    errorfile=open('errorinfo.txt','w')
    errorfile.write(traceback.format_exc())
    errorfile.close()
    print('The traceback info was written to errorinfo.txt')


#Logfile
#!/usr/bin/env python3
import logging
logging.basicConfig(filename='/Users/yangmingfan/Py2/Logfile.txt', level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)'%(n))
    total=1
    for i in range (1,n+1):
        total=total*i
        logging.debug('i is '+str(i)+',total is '+str(total))
    logging.debug('End of factorial(%s)'%(n))
    return total

print(factorial(5))
logging.debug('End of program')

#Download erro
import requests
res=requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as error:
    print('There was a problem: %s'%(error))

#DownloadtoFile
import requests
res=requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res.raise_for_status()
playfile=open('RomeoAndJuliet.txt','wb')
for chunk in res.iter_content(100000):
    playfile.write(chunk)
playfile.close()

#Download xkcd comics
import bs4, requests, os

from requests.models import parse_header_links
url='http://xkcd.com'
os.makedirs('/Users/yangmingfan/Py2/xkcd',exist_ok=True)
while not url.endswith('#'):
    print('Download page %s...' %url)
    res=requests.get(url)
    res.raise_for_status()

    soup=bs4.BeautifulSoup(res.text)
    
    comicelem=soup.select('#comic img')
    if comicelem==[]:
        print('could not find comic img.')
    else:
        comicUrl='http:'+comicelem[0].get('src')
        print('Downloading image %s' %(comicUrl))
        res=requests.get(comicUrl)
        res.raise_for_status()
        imagefile=open(os.path.join('/Users/yangmingfan/Py2/xkcd',os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(100000):
            imagefile.write(chunk)
        imagefile.close()
    prevlink=soup.select('a[rel="prev"]')[0]
    url='http://xkcd.com'+prevlink.get('href')
print('Done')

#google feeling lucky
import bs4, requests, webbrowser, sys
print('Googling...')
res=requests.get('http://google.com/search?q='+' '.join(sys.argv[1:]))
res.raise_for_status()
#print(res.status_code)
soup=bs4.BeautifulSoup(res.text)
linkelems=soup.select('.r a')
numopen=min(5,len(linkelems))
for i in range(numopen):
    webbrowser.open('http://google.com'+linkelems[i].get('href'))

#bs4 test
import bs4

examplefile=open('/Users/yangmingfan/Py2/example.html')

examplesoup=bs4.BeautifulSoup(examplefile.read())

elems=examplesoup.select('span')[1]

print(str(elems))

print(elems.get('class'))

print(elems.get('"html-tag">&lt;ht')==None)

print(elems.attrs)




import bs4

examplefile=open('/Users/yangmingfan/Py2/example.html')

examplesoup=bs4.BeautifulSoup(examplefile.read())

elems=examplesoup.select('span')

print(len(elems))

print(elems[0].getText)

print(str(elems[0]))

print(elems[0].attrs)


#selenium test
# from selenium import webdriver
# browser=webdriver.Edge('C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\Scripts\MicrosoftWebDriver.exe')
# browser.get('http://www.baidu.com')
# print(browser.page_source)
# browser.close()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.edge.service import Service
# s=Service('C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\Scripts\MicrosoftWebDriver.exe')
# browser= webdriver.Edge(service=s)
# browser.get('http://inventwithpython.com')
# print(browser.page_source)
# try:
#     elem=browser.find_element(By.CLASS_NAME,'card-title')
#     print('Found element with that calss name!')#%(elem.tag_name))
#     browser.quit()
# except:
#     print('Was not able to find an element with that name.')
#     browser.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.edge.service import Service
# s=Service('C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\Scripts\MicrosoftWebDriver.exe')
# browser= webdriver.Edge(service=s)
# browser.get('http://inventwithpython.com')
# linkelem=browser.find_element(By.LINK_TEXT,'Blog')
# print(type(linkelem))
# linkelem.click()


# from selenium import webdriver
# from selenium.webdriver.common import by
# from selenium.webdriver.common.by import By
# from selenium.webdriver.edge.service import Service
# s=Service('C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\Scripts\MicrosoftWebDriver.exe')
# browser= webdriver.Edge(service=s)
# browser.get('http://www.baidu.com')
# try:
#     textelems=browser.find_element(By.ID,'kw')
#     textelems.send_keys('12345')
# except:
#     print('failed')

#cmdmail
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
s = Service(r'/Users/yangmingfan/Library/Python/3.8/bin/chromedriver')
browser = webdriver.Chrome(service=s)
browser.get('http://mail.qq.com')

time.sleep(1)
browser.switch_to.frame('iframe')
email_elem = browser.find_element(By.NAME, 'email')
password_elem = browser.find_element(By.NAME, 'password')

email_elem.send_keys('278586884@qq.com')
password_elem.send_keys('qqhbc68119443')
login_elem = browser.find_element(By.ID, 'dologin')
login_elem.click()

time.sleep(1)
write_elem = browser.find_element(By.XPATH, '')
write_elem.click()

time.sleep(1)
recipient_elem = browser.find_element(By.XPATH, '')
recipient_elem.send_keys(sys.argv[1])

frame_elem = browser.find_element(By.XPATH, '')
browser.switch_to.frame(frame_elem)
content_elem = browser.find_element(By.XPATH, '')
content_elem.send_keys(sys.argv[2])

browser.switch_to.default_content()
send_elem = browser.find_element(By.XPATH, '')
send_elem.click()

time.sleep(1)
browser.quit()
