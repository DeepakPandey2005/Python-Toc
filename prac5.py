# design a program for creating a machine that accepts the string always ending with 101 

def accept_101(input_str):
    state=0
    for char in input_str:
        if state==0 and char=='0':
            pass
        elif state==0 and char=='1':
            state=1
        elif state==1 and char=='0':
            state=2
        elif state==2 and char=='1':
            state=3
        else:
             state=0
    return state==3

def check():
    input_str=input('enter the string')
    ans=accept_101(input_str)
    if(ans):
        print('accepted')
    else:
        print('rejected')

if __name__=="__main__":
    check()