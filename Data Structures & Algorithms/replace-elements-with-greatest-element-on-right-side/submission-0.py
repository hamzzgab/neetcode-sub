class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        temp = [-1] * len(arr)

        for i, num in enumerate(arr):
            if i != len(arr) - 1:
                temp[i] = max(arr[i + 1:])

        return temp