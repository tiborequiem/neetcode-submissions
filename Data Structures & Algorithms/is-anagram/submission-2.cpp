class Solution {
public:
    bool isAnagram(string s, string t) {
        

 if(s.size() != t.size()){
    return false;
 }


 unordered_map <int,int> mymap;

 for(char c : s){
    mymap[c]++;
 }

 for(char c : t ){
    mymap[c]--;
    if (mymap[c] < 0)
    return false;
 }

 return true;



    }
};
