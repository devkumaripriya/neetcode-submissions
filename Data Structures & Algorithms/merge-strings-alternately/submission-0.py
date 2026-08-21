
class Solution:
    
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3=''
        minLength=min(len(word1),len(word2))
        for i in range (minLength):
            word3 += word1[i]+word2[i]
        j=minLength
        if len(word1)>minLength:
            for j in range(len(word1)):
                word3 +=word1[j]
        elif len(word2)>minLength:
            for j in range(minLength,len(word2)):
                word3+=word2[j]
        return word3