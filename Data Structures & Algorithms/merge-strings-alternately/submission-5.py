
class Solution:
    
    def mergeAlternately(self,word1:str,word2:str)->str:
        word3='' # This will store our final answer
        minlength=min(len(word1),len(word2))# Find the length of the shorter string
    # Example: word1 = "abc" (3)
    #          word2 = "pqrs" (4)
    #          minlength = 3
        for i in range(minlength): # Take one character from word1
    # and one character from word2
            word3+=word1[i]+word2[i] # i = 0 → word1[0] + word2[0]
        # i = 1 → word1[1] + word2[1]
        # i = 2 → word1[2] + word2[2]
        j=minlength  # At this point, characters from index 0
    # up to minlength-1 have already been used
        if len(word1)>minlength:     # Check if word1 has remaining characters
            for j in range(minlength,len(word1)):   # Start from minlength, NOT 0
        # because indexes 0 to minlength-1 are already used
                word3+=word1[j]
        elif len(word2)>minlength:  # Otherwise, check if word2 has remaining characters
            for j in range(minlength,len(word2)): # Again, start from minlength
                word3+=word2[j]
        return word3 # Return the final merged string
