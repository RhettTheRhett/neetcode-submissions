#include <vector>
#include <list>


class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> hashTable;
        for(int i = 0; i < nums.size(); i++){
            int targetAdder = target - nums[i];

            if(hashTable.find(targetAdder) != hashTable.end()){
                return {hashTable[targetAdder], i};
            }

             hashTable[nums[i]] = i;
        }
    }
};
