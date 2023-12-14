# LRU

count_memory=int(input("Enter number of memory blocks : "))
seq=list(map(int,input("Enter a sequence ").split(' ')))

blocks=[None for _ in range(count_memory)]
timestamp=[-1 for _ in range(count_memory)]

hits=0
faults=0
head=0

for i,j in enumerate(seq):
    if j not in blocks:
        #page fault
        minimum=min(timestamp)
        index=timestamp.index(minimum)
        blocks[index]=j
        timestamp[index]=i
        faults+=1
    else:
      
        hits+=1
    print(j,":\t",blocks)

print(f"Hits : {hits} \n Faults : {faults}")