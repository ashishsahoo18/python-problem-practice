#include <algorithm>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> s(nums.begin(), nums.end());
        int best=0;
        for(int n:s){
            if(s.find(n-1) == s.end()){
                int length = 1;
                while(s.count(n+length)) length++;
                best=max(best,length);
            }
        }
        return best;
    }
};