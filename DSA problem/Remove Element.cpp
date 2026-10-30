#include <vector>

using namespace std;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        vector<int>::size_type k=0;
        for(vector<int>::size_type i=0; i<nums.size(); i++){
            if(nums[i] != val){
                nums[k++] = nums[i];
            }
        }
        return static_cast<int>(k);
    }
};