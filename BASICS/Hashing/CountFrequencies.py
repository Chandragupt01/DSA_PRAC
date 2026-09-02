def countFrequencies(nums):
    
        freq={}
        for num in nums:
                freq[num]=freq.get(num,0)+1
        result=[[k,v] for k,v in freq.items()]
        return result
              

nums=[1, 2, 2, 1, 3]
print(countFrequencies(nums))