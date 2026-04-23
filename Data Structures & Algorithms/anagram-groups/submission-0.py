class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for c in word:
                # abc
                # count[0, 0, 0, ..., 0]
                # count[1, 1, 1, 0, ..., 0]
                count[ord(c) - ord('a')] += 1
            anagrams[tuple(count)].append(word)
        
        return list(anagrams.values())

        







        
            





        