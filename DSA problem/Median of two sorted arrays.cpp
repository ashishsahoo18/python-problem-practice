
// 24.Median of Two Sorted Arrays

# include <vector>
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector <int> merged;
        int i=0;
        int j=0;

        while(i<nums1.size() && j<nums2.size()){
            if(nums1[i]<nums2[j]){
                merged.push_back(nums1[i]);
                i++;
            }else{
                merged.push_back(nums2[j]);
                j++;
            }
        }

        while(i<nums1.size()){
            merged.push_back(nums1[i]);
            i++;
        }

        while(j<nums2.size()){
            merged.push_back(nums2[j]);
            j++;
        }

        int n=merged.size();

        if(n % 2 == 1){
            return merged[n/2];
        }
        else{
            return (merged[n/2 -1] + merged[n/2]) / 2.0;
        }
        
    }
};

// Palindrome Number

class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0){
            return false;
        }
        long long reverse = 0;
        int original = x;
        while(x>0){
            int digit = x % 10;
            reverse = reverse * 10 + digit;
            x = x/10;
        }
        return original==reverse;
    }
    
};