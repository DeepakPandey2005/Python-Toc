# design a program for creating a machine that accepts the string having equal no of 1s and 0s 

def chkEqual01(input_str):
    zero=one=0
    for char in input_str:
        if char=='0':
            zero+=1
        elif char=='1':
            one+=1
    if (zero == one):
        print("The number is accepted")
    else:
        print("The number is not accepted")

if __name__=="__main__":
    inputStr=input("enter the string to check : ")
    if all(i in '01' for i in inputStr):
        chkEqual01(inputStr)
    else:
        print("you have given wrong input")
