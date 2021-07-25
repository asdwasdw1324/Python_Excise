#Case1_collatz
def collatz(number):
    if number%2==0:
        print(number//2)
        n=number//2
    else:
        print(3*number+1)
        n=3*number+1
    return n
#定义collatz函数
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
