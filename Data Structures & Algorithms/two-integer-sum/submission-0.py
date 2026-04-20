class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mydict = {}

        for i in range(len(nums)):

            converse = target - nums[i]

            if converse in mydict:
                return [mydict[converse], i]
            
            else:
                mydict[nums[i]] = i
            
