#program for Tokenization of the given input 

def cutom_tokens(input_text):
    tokens =[]
    curr_token=""

    for char in input_text:
        if char.isalnum() or char=="_":
            curr_token+=char

        elif curr_token:
            tokens.append(curr_token)
            curr_token=""

    if curr_token:
        tokens.append(curr_token)
        return tokens
    
def tokenize_all_char(input_text):
    return list(input_text)

if __name__=="__main__":
    input_text=input("enter the string ")

    word_tokens=cutom_tokens(input_text)
    char_tokens=tokenize_all_char(input_text)

    print("tokenize word are ")
    print(word_tokens)
    print("\n tokenize char are")
    print(char_tokens)


