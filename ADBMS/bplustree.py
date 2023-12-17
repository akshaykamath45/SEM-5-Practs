from bplustree import BPlusTree
import time

tempfile="C:\\Users\\Akshay Kamath\\Desktop\\practice\\bppc.txt"
bptree=BPlusTree(order=2,filename=tempfile)

def user_input():
    print("--------B Tree----------")
    print("1. for Insertion")
    print("2. for Search")
    print("3. for Show")
    print("4. for Ext")

    return str(input("Enter your choice : "))

def encode_value(value):
    return value.to_bytes((value.bit_length()+7)//8,'big')
def decode_value(encode_value):
    return int.from_bytes(encode_value,'big')
while True:
    user_choice=user_input()
    if(user_choice=='1'):
        n=int(input("Enter a number : "))
        encoded_value=encode_value(n)
        bptree[n]=encode_value
        print(f"{n} inserted successfully")
    if(user_choice=='2'):
        n=int(input("Search a number : "))
        found_value=bptree.get(n)
        if found_value is not None:
            decoded_value=decode_value(found_value)
            
        else:
            print(f"{n} not found")
        
    if(user_choice=='3'):
        for ele in bptree.items():
            print(ele,end=' ')
        print("\n")
   
    elif(user_choice=='4'):
        exit()