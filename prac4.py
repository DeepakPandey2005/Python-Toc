# design a program for creating a machine that accepts three consecutive ones over 0 and 1 

def Check(string):
    state=0
    for digit in string:
        if state==0 and digit=='0':
            pass
        elif state==0 and digit=='1':
            state=1
        elif state==1 and digit=='1':
            state=2
        elif state==2 and digit=='1':
            return True
        else:
            state=0
    return False

def check():
    inputStr=input("enter the binary numbers")
    ans =Check(inputStr)
    if(ans):
        print('accepted')
    else:
        print('rejected')
        
if __name__=='__main__':
    check()
    