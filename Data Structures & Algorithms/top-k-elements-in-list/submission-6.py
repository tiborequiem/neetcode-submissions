class Solution:
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        heap_min= []

        for num , freq in count.items():
            heapq.heappush(heap_min, (freq, num))
            if len(heap_min) > k:
                heapq.heappop(heap_min)

        result = [num for freq, num in heap_min]     

        return result   



        