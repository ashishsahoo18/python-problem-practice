#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
       unordered_map<long long,int>mp;
       for(vector<int>::size_type i=0; i<nums.size(); i++){
        long long need= static_cast<long long>(target)-nums[i];
        if(mp.find(need) != mp.end()){
            return{mp[need],static_cast<int>(i)};
        }
        mp[nums[i]]=static_cast<int>(i);
       } 
       return{};
    }
};