class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        
        def indexes(substr):
            result = list()
            i = 0
            while(True):
                found_index = s.find(substr, i)
                if (found_index == -1):
                    break
                result.append(found_index)
                i = found_index + 1
            return result
        
        i1 = indexes(a)
        i2 = indexes(b)
        
        answer = []
        j = 0
        for i in i1:
            while j < len(i2) and i2[j] < i - k:
                j += 1
            if j == len(i2):
                break
            if i2[j] > i + k:
                continue
            answer.append(i)
        return answer
