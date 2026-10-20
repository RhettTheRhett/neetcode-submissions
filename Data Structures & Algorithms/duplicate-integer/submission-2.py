class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}
        dupe = False
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 0
            num_dict[num] += 1
            if(num_dict[num] > 1): 
                return True
             
        return False

        