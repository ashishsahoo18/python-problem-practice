// Q) Sample Input 1

// 17 28 30
// 99 16 8
// Sample Output 1

// 2 1

// (Code in c++) 

include <bits/stdc++.h>
using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

vector<int> compareTriplets(vector<int> a, vector<int> b) {
    int Alice = 0;
    int Bob = 0;
    for(int i = 0; i<3; i++){
        if(a[i] > b[i]){
            Alice++;
        }
        else if(a[i] < b[i]){
            Bob++;
        }
    }
    return {Alice , Bob};
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string a_temp_temp;
    getline(cin, a_temp_temp);

    vector<string> a_temp = split(rtrim(a_temp_temp));

    vector<int> a(3);

    for (int i = 0; i < 3; i++) {
        int a_item = stoi(a_temp[i]);

        a[i] = a_item;
    }

    string b_temp_temp;
    getline(cin, b_temp_temp);

    vector<string> b_temp = split(rtrim(b_temp_temp));

    vector<int> b(3);

    for (int i = 0; i < 3; i++) {
        int b_item = stoi(b_temp[i]);

        b[i] = b_item;
    }

    vector<int> result = compareTriplets(a, b);

    for (size_t i = 0; i < result.size(); i++) {
        fout << result[i];

        if (i != result.size() - 1) {
            fout << " ";
        }
    }

    fout << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}


// Q) Sample Input

// STDIN                                                   Function
// -----                                                   --------
// 5                                                       arr[] size n = 5
// 1000000001 1000000002 1000000003 1000000004 1000000005  arr[...]  
// Output

// 5000000015

include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);



long aVeryBigSum(vector<long> ar) {
    long sum = 0;
    for(int i=0; i<ar.size(); i++){
        sum = sum+ar[i];
    }
    return sum;

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string ar_count_temp;
    getline(cin, ar_count_temp);

    int ar_count = stoi(ltrim(rtrim(ar_count_temp)));

    string ar_temp_temp;
    getline(cin, ar_temp_temp);

    vector<string> ar_temp = split(rtrim(ar_temp_temp));

    vector<long> ar(ar_count);

    for (int i = 0; i < ar_count; i++) {
        long ar_item = stol(ar_temp[i]);

        ar[i] = ar_item;
    }

    long result = aVeryBigSum(ar);

    fout << result << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}



// Sample Input:-
// STDIN           Function
// -----           --------
// 6               ar[] size n = 6
// 1 2 3 4 10 11   ar = [1, 2, 3, 4, 10, 11]
// Sample Output:-
//         31

include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'simpleArraySum' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY ar as parameter.
 */

int simpleArraySum(vector<int> ar) {
    int total = 0;
    for(int i=0; i< ar.size(); i++){
        total = total + ar[i];
    }
    return total;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string ar_count_temp;
    getline(cin, ar_count_temp);

    int ar_count = stoi(ltrim(rtrim(ar_count_temp)));

    string ar_temp_temp;
    getline(cin, ar_temp_temp);

    vector<string> ar_temp = split(rtrim(ar_temp_temp));

    vector<int> ar(ar_count);

    for (int i = 0; i < ar_count; i++) {
        int ar_item = stoi(ar_temp[i]);

        ar[i] = ar_item;
    }

    int result = simpleArraySum(ar);

    fout << result << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}


// Sample Input:-
//       4 3
//       <tag1 value = "HelloWorld">
//       <tag2 name = "Name1">
//       </tag2>
//       </tag1>
//       tag1.tag2~name
//       tag1~name
//       tag1~value
// Sample Output:-
//       Name1
//       Not Found!
//       HelloWorld


include <cmath>
include <cstdio>
include <vector>
include <iostream>
include <sstream>
include <map>
include <algorithm>
using namespace std;


int main() {
    int n,q;
    cin>> n >> q;
    cin.ignore();
    
    map<string,string> attributes;
    vector<string> path;
    
    for(int i=0; i<n; i++){
        string line;
        getline(cin,line);
        
        if(line[1] == '/'){
            path.pop_back();
            continue;
        }
        
        line = line.substr(1, line.size()-2 );
        
        stringstream ss(line);
        
        string tag;
        ss>>tag;
        path.push_back(tag);
        
        string currentPath = "";
        
        for(size_t j=0; j<path.size(); j++){
            if(j>0){
                currentPath += ".";
            }
            currentPath += path[j];
        }
        
        string attribute, equal, value;
        
        while(ss>>attribute>>equal>>value){
            value = value.substr(1,value.size()-2);
            
            string key = currentPath + "~" + attribute;
            
            attributes[key] = value;
        }
    }  
    
    for(int i=0; i<q; i++){
        string query;
        getline(cin,query);
        
        if(attributes.find(query) != attributes.end()){
            cout<<attributes[query]<<endl;
        }
        else{
            cout<<"Not Found!"<<endl;
        }
    }
    return 0;
}



Sample Input :-
5 6 7
3 6 10
Sample Output:-
1 1
Answer:
vector<int> compareTriplets(vector<int> a, vector<int> b) {
    int Alice = 0;
    int Bob = 0;
    for(int i = 0; i<3; i++){
        if(a[i] > b[i]){
            Alice++;
        }
        else if(a[i] < b[i]){
            Bob++;
        }
    }
    return {Alice , Bob};


Median of Two Sorted Arrays


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