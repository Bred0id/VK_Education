import heapq

def mergeKSortedArrays(sortedArrays):
    mergedArray = []
    minHeap = []
    for i in range(len(sortedArrays)):
        currentArray = sortedArrays[i]
        if len(currentArray) > 0:
            heapq.heappush(minHeap, (currentArray[0], i, 0))
    while len(minHeap) > 0:
        value, arrayIdx, elementIdx = heapq.heappop(minHeap)
        mergedArray.append(value)
        if elementIdx + 1 < len(sortedArrays[arrayIdx]):
            nextElement = sortedArrays[arrayIdx][elementIdx + 1]
            heapq.heappush(minHeap, (nextElement, arrayIdx, elementIdx + 1))
    return mergedArray