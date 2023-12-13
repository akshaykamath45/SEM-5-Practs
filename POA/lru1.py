count_memory=int(input("ENter number of memory blocks : "))
seq=list(map(int,input("Enter a sequence : ").split(' ')))

hits=0
faults=0
block=[None for _ in range(count_memory)]
timestamp=[-1 for _ in range(count_memory)]
for i,j in enumerate(seq):
    if j not in block:
        #page fault
        minimum=min(timestamp)
        index=timestamp.index(minimum)

        block[index]=j
        timestamp[index]=i
        faults+=1
    else:
        #page hit
        index=block.index(j)
        timestamp[index]=i
        hits+=1
    print(j,"\t",block)

print(f"Hits {hits}")
print(f"Faults {faults}")