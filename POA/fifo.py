# Get the number of memory blocks and the sequence of page references from the user
count_memory = int(input("Enter no. of memory blocks: "))
seq = list(map(int, input("Enter the sequence: ").split(' ')))

# Initialize memory blocks
block = [None for _ in range(count_memory)]

# Initialize hit, fault counters, and head pointer
hits = 0
faults = 0
head = 0

# Iterate through the page reference sequence
print()
for j in seq:
    # Check if the page is not in memory
    if j not in block:
        # Replace the block at the head position with the new page
        block[head] = j
        head = (head + 1) % count_memory  # Update head pointer in a circular manner
        faults += 1  # Increment fault counter
    else:
        hits += 1  # Increment hit counter
    
    # Print the current page and the memory block state
    print(j, " : \t", block)

# Display the results
print(f"\nNo. of hits: {hits}\t\tHit ratio: {hits / len(seq)}")
print(f"No. of faults: {faults}\tFault ratio: {faults / len(seq)}")
