# Design a program for accepting decimal number divisible by 2

def checkDivBy2(input_str):
    state='q0'
    for digit in input_str:
        if state=='q0':
            if digit in '02468':
                state='q0'
            elif digit in '13579':
                state='q1'
            else:
                return False

        elif state=='q1':
            if digit in '02468':
                state='q0'
            elif digit in '13579':
                state='q1'
            else:
                return False
    return state=='q0'
if __name__=="__main__":
    inputStr=input("enter the number")
    ans=checkDivBy2(inputStr)
    if(ans):
        print(f"the number {inputStr} is divisible by 2 ")
    else:
        print(f"the number {inputStr} is not divisible by 2")
