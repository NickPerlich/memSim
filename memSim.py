# imports
from collections import deque

# constants
BLOCK_SIZE = 256
TLB_SIZE = 16

class TLB:
    def __init__(self, entries=None, oldest=0):
        if entries is None:
            entries = [None] * TLB_SIZE
        self.entries = entries
        self.oldest = oldest

    def insert(self, new):
        # check for empty slots in the TLB
        if self.entries[self.oldest] is None:
            self.entries[self.oldest] = new
            # if the TLB has filled up, point to first entry as the oldest
            if self.oldest + 1 >= TLB_SIZE:
                self.oldest = 0
            else:
                self.oldest += 1
        # all slots are filled, now we replace using FIFO
        else:
            self.entries[self.oldest] = new
            if self.oldest + 1 >= TLB_SIZE:
                self.oldest = 0
            else:
                self.oldest += 1


tlb = TLB()
tlb_stream = [None] 

for entree in tlb_stream:
    tlb_stream[entree] = tlb_entry(1, 1)

for entree in tlb_stream