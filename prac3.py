# program for generating derivation sequence language for the given sequence of productions

def generate_string(n):
    if n>0:
        return 'a'*n+'b'*n
    
if __name__=="__main__":
    while True:
        try:
            n=int(input("enter the value of n :"))
            ans=generate_string(n)
            print(f"Generate string for n={n} = {ans}")
            break
        except ValueError:
            print("Invalid input . please enter a valid integer for n")
    