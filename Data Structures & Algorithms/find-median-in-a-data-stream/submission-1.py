import heapq
class MedianFinder:

    def __init__(self):
        self.count = 0
        self.maxHeap = []
        self.minHeap = []
        

    def addNum(self, num: int) -> None:
        self.count += 1
        heapq.heappush(self.maxHeap, -1*num)
        # if self.count  == 3:
        #     print(self.maxHeap, self.minHeap)
        while self.minHeap and -1*self.maxHeap[0] > self.minHeap[0]:
            min_ele = heapq.heappop(self.minHeap)
            max_ele = -1*heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, max_ele)
            heapq.heappush(self.maxHeap, -1*min_ele)
        
        # if self.count  == 3:
        #     print(self.maxHeap, self.minHeap)

        mid = self.count // 2
        while len(self.maxHeap) > mid:
            heapq.heappush(self.minHeap, -1*heapq.heappop(self.maxHeap))
        
        # if self.count  == 3:
        #     print(self.maxHeap, self.minHeap)
            
    def findMedian(self) -> float:
        if self.count % 2 == 0:
            return (self.minHeap[0] + (-1*self.maxHeap[0])) / 2
        else:
            # print(self.maxHeap, self.minHeap)
            return float(self.minHeap[0])
        
        