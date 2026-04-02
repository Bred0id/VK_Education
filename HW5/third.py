import heapq

def kthSmallest(arr, k):
    if k <= 0 or k > len(arr):
        return None
    maxHeap = []
    for num in arr:
        heapq.heappush(maxHeap, -num)
        if len(maxHeap) > k:
            heapq.heappop(maxHeap)
    return -maxHeap[0]

def kthLargest(arr, k):
    if k <= 0 or k > len(arr):
        return None
    minHeap = []
    for num in arr:
        heapq.heappush(minHeap, num)
        if len(minHeap) > k:
            heapq.heappop(minHeap)
    return minHeap[0]