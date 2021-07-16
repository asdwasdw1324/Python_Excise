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
