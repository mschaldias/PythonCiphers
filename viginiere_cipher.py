
# coding: utf-8

# In[ ]:


# Viginiere Cipher

s = '''0123456789,.?!':"' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'''


def build_table():
    letter_li = []
    dic = {}
    for letter in s:
        letter_li.append(letter)
 
    
    for i,letter in enumerate(letter_li):
        dic[letter] = letter_li[i:] + letter_li[:i]

    return dic

def encrypt(key,msg,table):

    key_rep = ""
    code = ""
    
    i = 0
    
    for letter in msg:   
        
        key_rep += key[i]
        i += 1
            
        if i == len(key):  
            i = 0

    
    
    for i,letter in enumerate(key_rep):
        row = table[letter]
        
        msg_letter = msg[i]
        j = s.index(msg_letter)
        
        code += row[j]
        
    return code,key_rep
    
def decrypt(key,code,table):
    
    decode =""
    key_rep = ""
    
    i = 0
    
    for letter in code:   
        
        key_rep += key[i]
        i += 1
            
        if i == len(key):  
            i = 0
    
    
    for i,letter in enumerate(key_rep):
        
        row = table[letter]
        
        code_letter = code[i]
        
        j = row.index(code_letter)
        
        decode += s[j]
        
    return decode,key_rep


def main():
    
    table = build_table()
    running = True

    while running:
    
        key = input("Key: ")

        
        msg = input("Message: ")


        mode = input("Encode or decode? (e/d)")

        if mode == 'e':
            result,key_rep = encrypt(key,msg,table)

        elif mode == 'd':
            result,key_rep = decrypt(key,msg,table)
        
        print(result)
        print(key_rep)
        
        cont = input("Continue? (y/n) ")
        if cont == "n":
            return
        
    
main()

