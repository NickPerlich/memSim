# imports
from collections import deque

# constants
FRAME_SIZE = 256
TLB_SIZE = 16

tlb = deque()


def fifo(memory, new: str):
    mem = deque(memory)
    mem.popleft()  # pop the oldest item
    mem.append(new)  # push the new item
    return list(mem)


def lru(memory: deque, new: str, capacity: int) -> deque:
    if new in memory:
        memory.remove(new)       # Page already in memory → move to MRU
    elif len(memory) >= capacity:
        memory.popleft()         # Memory full → remove LRU (leftmost)

    memory.append(new)           # Add to MRU position (rightmost)
    return memory


memory = ['a', 'b', 'c']

input = ['a', 'b', 'c', 'a', 'd', 'b', 'e']

memory = deque(memory)
for i in input:
    print(i)
    memory = lru(memory, i, 3)
    print(memory)


