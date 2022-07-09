def twoSum(self, nums, target):
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      sum = [i] + [j]
     if sum == target:
      return[i,j]
    
    
