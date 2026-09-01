class Solution:
    def reverse(self, arr: list, n: int) -> None:
        def helper(left,right):
            if left>=right:
                return
            arr[left],arr[right]=arr[right],arr[left]
            return helper(left+1,right-1)
        return helper(0,len(arr)-1)