#Experiments:

import random


original = "0123456789abcdefghi jklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.!?:"


def scramble(seed):

    c_li = []

    for c in original:
        c_li.append(c)

    o_li = c_li[:]


    random.seed(seed)

    random.shuffle(c_li)

    return o_li,c_li

def dictionary(o_li,c_li):

    
    encoding={}
    decoding={}
    
    for i,char in enumerate(o_li):
        encoding[char] = c_li[i]
    
    for i,char in enumerate(c_li):
        decoding[char] = o_li[i]
        
        
    return encoding,decoding

def process(coding,message):
    
    result = ""
    for char in message:
        result += coding[char]
    print(result)
        


def main():
    

    stop = False
    seed = input("Seed: ")
    while stop == False:
        
        if seed == "":  
            seed = random.randint(0,1000)
            print(seed)
        
        o_li,c_li = scramble(seed)
        encoding,decoding = dictionary(o_li,c_li)        

        
        message = input("Message: ")
        
        if message == "":
            stop = False
            print("Exiting...")
            break
            
        mode = input("Encode/Decode?(e/d) ")

        if mode == "e":
            process(encoding,message)

        elif mode == "d":
            process(decoding,message)

    input()
main()