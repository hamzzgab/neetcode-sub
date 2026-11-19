# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:

    def merge(self, pairs, start, mid, end):
        L = pairs[start:mid+1]
        R = pairs[mid+1:end+1]
        i = j = 0
        k = start

        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                pairs[k] = L[i]
                i += 1
            else:
                pairs[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            pairs[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            pairs[k] = R[j]
            j += 1
            k += 1


    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        def recursive(pairs, start, end):
            if end - start + 1 <= 1:
                return pairs

            mid = (start + end) // 2
            recursive(pairs, start, mid)
            recursive(pairs, mid + 1, end)
            self.merge(pairs, start, mid, end)
            return pairs

        return recursive(pairs, 0, len(pairs)-1)
