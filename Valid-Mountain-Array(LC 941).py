class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # check for only arrays with length greater than 3
        if len(arr) < 3:
            return False
        
        #check for the max element in the array
        peak = max(arr)
        
        #return False if the max element is at any end of the array
        if peak == arr[len(arr)-1] or peak == arr[0]:
            return False
        
        #return False if the left side is not strictly increasing
        for j in range(arr.index(peak)):
            if arr[j] >= arr[j+1]:
                return False
            
        #return False if the right side is not strictly decreasing
        for k in range(arr.index(peak)+1,len(arr)):
            if arr[k-1] <= arr[k]:
                return False
        
        return True
