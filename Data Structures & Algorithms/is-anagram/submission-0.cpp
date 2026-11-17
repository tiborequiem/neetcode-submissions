class Solution {
public:
    bool isAnagram(string s, string t) {
        



int temp;

for(int i = 0 ; i < s.size() - 1 ; i++){
    for(int j = 0 ; j < s.size() - i - 1 ; j++) {
        
        if(s[j] > s[j+1]){
            temp = s[j];
            s[j] = s[j+1];
            s[j+1] = temp;
        }
        
    }
}


for(int i = 0 ; i < t.size() -1 ; i++){
    for(int j = 0 ; j < t.size() - i -1 ; j++){
        
        if(t[j] > t[j+1]){
            temp = t[j];
            t[j] = t[j+1];
            t[j+1] = temp;
        }
        
    }
}


cout<< t << endl<< s<<endl;



if(s.compare(t) == 0){
    return true;;
}

else
return false;




    }
};
