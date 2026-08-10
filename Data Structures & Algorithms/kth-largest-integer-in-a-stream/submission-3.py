class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []    # min-heap 
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        self.heap.append(val)
        self.percolateUp()
        while len(self.heap) > self.k:
            self.remove()
        return self.heap[0]

    def remove(self) -> None:
        val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.percolateDown()
        return val

    def getParentIndex(self, i):
        if i == 0:
            return 0
        return (i - 1) // 2

    def getChildIndices(self, i):
        l = (i * 2) + 1
        r = (i * 2) + 2
        l = l if l < len(self.heap) else None
        r = r if r < len(self.heap) else None
        return l, r

    def percolateDown(self) -> None:
        index = 0
        l, r = self.getChildIndices(index)

        while (l is not None and self.heap[index] > self.heap[l]) or (r is not None and self.heap[index] > self.heap[r]):
            smaller = index
            if l is not None and self.heap[l] < self.heap[smaller]:
                smaller = l
            if r is not None and self.heap[r] < self.heap[smaller]:
                smaller = r

            self.heap[index], self.heap[smaller] = self.heap[smaller], self.heap[index]
            index = smaller
            l, r = self.getChildIndices(index)
        return             

    def percolateUp(self) -> None:
        index = len(self.heap) - 1
        p = self.getParentIndex(index)
        while index > 0 and self.heap[p] >= self.heap[index]:
            self.heap[p], self.heap[index] = self.heap[index], self.heap[p]
            index = p
            p = self.getParentIndex(index)
        return None
        

        
