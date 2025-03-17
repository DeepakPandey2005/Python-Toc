# design a program for creating a machine which count no of 1s and 0s in a given string 

def count01(inputStr):
    zero=one=0
    for char in inputStr:
        if char=='1':
            one+=1
        elif char=='0':
            zero+=1
    print(f"The number of zero is {zero}")
    print(f"The number of one is {one}")

def chk():
    inputStr=input("enter the number in 0 and 1 :")
    if all(i in '01' for i in inputStr):
        count01(inputStr)
    else:
        print("you have entered the wrong input give binary numbers")

if __name__=="__main__":
    chk()
 
        

