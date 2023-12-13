count_memory=int(input("Enter number of memory blocks : "))
seq=list(map(int,input("Enter a sequence ").split(' ')))

block=[None for _ in range (count_memory)]

hits=0
faults=0
head=0

for i,j in enumerate(seq):
    if j not in block:
        
        block[head]=j
        head=(head+1)%count_memory
        
        faults+=1
    else:
        hits+=1
    print(j," :\t",block)
    
print(f"Hits : {hits} \n Faults: {faults}")