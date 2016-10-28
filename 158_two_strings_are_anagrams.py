import array
import string

class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        sarr = array.array('i', (0 for i in range(0, 256) ) )
        for ch in s:
        	sarr[ord(ch)] += 1
        tarr = array.array('i', (0 for i in range(0, 256) ) )
        for ch in t:
        	tarr[ord(ch)] += 1
       	return tarr == sarr

if __name__ == "__main__":
	solution=Solution()
	print solution.anagram("ab", "baa")