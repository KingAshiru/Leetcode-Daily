class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        peak = max(arr)
        if peak == arr[len(arr)-1] or peak == arr[0]:
            return False
        
        for j in range(arr.index(peak)):
            if arr[j] >= arr[j+1]:
                return False
        
        for k in range(arr.index(peak)+1,len(arr)):
            if arr[k-1] <= arr[k]:
                return False
        
        return True
