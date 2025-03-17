# Design a PDA (pushdown automata) to accepts wcwr where w is any string and wr is reverse of that string and c is special symbol 

class PDA:
    def __init__(self):
        self.stack=[]

    def reset(self):
        self.stack=[]

    def process(self,string,seperator):
        state='q0'
        for char in string:
            if state=='q0':
                if char==seperator:
                    if not self.stack:
                        return False
                    state='q1'
                else:
                    self.stack.append(char)



            elif state=='q1':
                if self.stack and self.stack[-1]==char:
                    self.stack.pop()
                else:
                    return False
        return state=='q1' and not self.stack

def main():
        pda=PDA()
        test_cases=[
            ('abaCaba','C'),
            ('abcCab',"C"),
            ('aaaCaaa',"C"),
            ('C',"C"),
            ('abcddccba',"C"),
            ('aabDbaa','D')
        ]
        for string,separator in test_cases:
            pda.reset()

            ans=pda.process(string,separator)
            print(f"string {string} | Accepted:{ans}")
if __name__=="__main__":
        main()
    
                