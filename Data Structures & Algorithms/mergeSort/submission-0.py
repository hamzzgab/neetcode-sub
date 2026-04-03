# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def merge(self, arr, start, mid, end):
        left = arr[start:mid+1]
        right = arr[mid+1:end+1]
        
        l, r, i = 0, 0, start

        while l < len(left) and r < len(right):
            if left[l].key <= right[r].key:
                arr[i] = left[l]
                l+=1
            else:
                arr[i] = right[r]             
                r+=1
            i+=1
        
        while l<len(left):
            arr[i]=left[l]
            i+=1
            l+=1

        while r<len(right):
            arr[i]=right[r]
            i+=1
            r+=1
        return arr                

    def divide(self, arr, start, end):
        if (end-start+1) <= 1:
            return arr
        mid = (start + end) // 2
        self.divide(arr, start, mid)
        self.divide(arr, mid+1, end)
        self.merge(arr, start, mid, end)
        return arr

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.divide(pairs, 0, len(pairs) - 1)
