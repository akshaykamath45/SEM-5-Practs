# Get the number of memory blocks and the sequence of page references from the user
count_memory = int(input("Enter no. of memory blocks: "))
seq = list(map(int, input("Enter the sequence: ").split(' ')))

# Initialize memory blocks and timestamp lists
block = [None for _ in range(count_memory)]
timestamp = [-1 for _ in range(count_memory)]  


hits = 0
faults = 0

# Iterate through the page reference sequence
for i, j in enumerate(seq):
    # Check if the page is not in memory
    if j not in block:
        # Find the index of the block with the minimum timestamp
        minimum = min(timestamp)
        index = timestamp.index(minimum)
        
        # Replace the block at the found index with the new page
        block[index] = j
        timestamp[index] = i  # Corrected variable name
        faults += 1  # Increment fault counter
    else:
        # If the page is in memory, update its timestamp
        index = block.index(j)
        timestamp[index] = i  
        hits += 1  # Increment hit counter
    
    # Print the current page and the memory block state
    print(j, " : \t", block)

# Display the results
print(f"\nNo. of hits: {hits}\t\tHit ratio: {hits / len(seq)}")
print(f"No. of faults: {faults}\tFault ratio: {faults / len(seq)}")
