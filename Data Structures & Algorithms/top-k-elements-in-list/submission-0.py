class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        result = []

        for num in nums:
            freq[num] += 1

        # nums = [1,2,2,3,3,3]
        # freq = {1: 1, 2: 2, 3:3}

        # nums = [7,7]
        # freq = {7: 2}

        for i in range(k):
            # append key where value is max
            max_key = max(freq, key=freq.get)
            result.append(max_key)
            # pop key and value
            freq[max_key] = 0

        return result













        