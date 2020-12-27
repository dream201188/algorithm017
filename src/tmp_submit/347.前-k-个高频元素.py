#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [e[0] for e in collections.Counter(nums).most_common(k)]


    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = collections.Counter(nums)
        heap, ans = [], []
        for i in dic:
            heapq.heappush(heap, (-dic[i], i))
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans

   # 最佳效率 n*logk
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = collections.Counter(nums)
        heap, ans = [], []
        for i in dic:
            size = len(heap)
            if size == k:
                if heap[0][0] < dic[i]:
                    heapq.heapreplace(heap, (dic[i], i))
            else:
                heapq.heappush(heap, (dic[i], i))
        for _ in range(k):
            ans.append(heap.pop()[1])
        return ans


# @lc code=end

