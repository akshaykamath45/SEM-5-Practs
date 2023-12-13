def first_fit(memory_blocks,process_sizes):
    for (process_id,process_size) in enumerate(process_sizes):
        allocated=False
        for (i,block_size) in enumerate(memory_blocks):
            if(block_size>=process_size):
                memory_blocks[i]-=process_size
                print(f"Process {process_id} {process_size} allocated to block {i}")
                allocated=True
                break
               
        if not allocated:
            print(f"Process {process_id} {process_size} cannot be allocated to any block")
                
memory_blocks = [100, 500, 200, 300, 600]
process_sizes = [212, 417, 112, 426]

first_fit(memory_blocks, process_sizes)