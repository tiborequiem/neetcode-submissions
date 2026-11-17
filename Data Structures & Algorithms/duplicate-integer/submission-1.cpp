class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {



      
  unordered_map<int,int>MyMap;


 for(int i = 0; i < nums.size() ; i++ ){
  int X = MyMap[nums[i]]++;
   
  if (X >= 1){
      cout<<"True";
  return true;
  }

 }
 
 
cout<<"FALSE";
 return false;


    }
};