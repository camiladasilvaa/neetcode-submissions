class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in range(len(strs)):
            result += strs[i] + "*-*"
        
        return result


    def decode(self, s: str) -> List[str]:
        my_list = s.split("*-*")
        my_list.pop()
        return my_list


