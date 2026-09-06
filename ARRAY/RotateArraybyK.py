# TLE code
# class Solution:
#     def rotate(self, nums: list[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n=len(nums)
#         rotation=k%n
#         for i in range(rotation):
#             temp=nums.pop()
#             nums.insert(0,temp)


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k==0 or len(nums)==1:
            return
        def reverse(arr:list[int],start,end):
            i,j=start,end
            while i<j:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
                j-=1
            return arr
        n=len(nums)
        rotation=k%n
        reverse(nums,0,n-1)
        reverse(nums,0,rotation-1)
        reverse(nums,rotation,n-1)