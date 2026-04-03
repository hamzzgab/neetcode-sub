# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def merge(self, pairs, start, mid, end):
        left, right = pairs[start:mid+1], pairs[mid+1:end+1]
        l, r, k = 0, 0, start

        while l < len(left) and r < len(right):
            if left[l].key <= right[r].key:
                pairs[k] = left[l]
                l += 1
            else:
                pairs[k] = right[r]
                r += 1
            k += 1

        while l < len(left):
            pairs[k] = left[l]
            l += 1
            k += 1

        while r < len(right):
            pairs[k] = right[r]
            r += 1
            k += 1

        return pairs


    def divide(self, pairs, start, end):
        if end - start + 1 <= 1:
            return pairs
        
        mid = (start + end) // 2
        self.divide(pairs, start, mid)
        self.divide(pairs, mid + 1, end)
        self.merge(pairs, start, mid, end)

        return pairs

    def mergeSort(self, pairs):
        return self.divide(pairs, 0, len(pairs))

