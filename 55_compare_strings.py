import array

class Solution:
    """
    @param A : A string includes Upper Case letters
    @param B : A string includes Upper Case letters
    @return :  if string A contains all of the characters in B return True else return False
    """
    def compareStrings(self, A, B):
        Aarr = array.array('i', (0 for i in range(0, 26) ) )
        for ch in A:
        	Aarr[ord(ch)-ord('A')] += 1
        Barr = array.array('i', (0 for i in range(0, 26) ) )
        for ch in B:
        	Barr[ord(ch)-ord('A')] += 1
        for i in range(0, 26):
        	if Aarr[i] < Barr[i]:
        		return False
        return True

if __name__=="__main__":
	solution=Solution()
	print solution.compareStrings("ABCD", "AACD")