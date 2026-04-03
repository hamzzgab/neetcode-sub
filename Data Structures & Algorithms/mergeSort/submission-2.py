# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def merge(self, pairs, s, m, e):
        L, R = pairs[s : m+1], pairs[m+1 : e+1]
        l, r, i = 0, 0, s



        while l < len(L) and r < len(R):
            if L[l].key <= R[r].key:
                pairs[i] = L[l]
                l += 1
            else:
                pairs[i] = R[r]
                r += 1
            i += 1

        while l < len(L):
            pairs[i] = L[l]
            l += 1            
            i += 1

        while r < len(R):        
            pairs[i] = R[r]
            r += 1
            i += 1
        return pairs

    def divide(self, pairs, s, e):
        if (e - s + 1) <= 1:
            return pairs

        m = (e + s) // 2    
        self.divide(pairs, s, m)
        self.divide(pairs, m + 1, e)

        print(self.show(pairs))

        return self.merge(pairs, s, m, e)


    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.divide(pairs, 0, len(pairs) - 1)

    
    def show(self, pairs):
        return [pair.key for pair in pairs]
