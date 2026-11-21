class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS = {}
        hashT = {}
        for char in s:
            if char not in hashS:
                hashS[char] = 1 
            else:
                hashS[char] = hashS[char] + 1    

        for char in t:
            if char not in hashT:
                hashT[char] = 1
            else:
                hashT[char] = hashT[char] + 1

        return hashS == hashT        







