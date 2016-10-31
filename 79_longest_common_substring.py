class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        res = 0
        matchingMap=[[0 for i in range(1000)] for j in range(1000)]
        for i in range(1, len(A)+1):
            for j in range(1, len(B)+1):
                if A[i-1]==B[j-1]:        
                    matchingMap[i][j]=matchingMap[i-1][j-1]+1
                    res=max(matchingMap[i][j], res)
                else:
                    matchingMap[i][j]=0
        return res

if __name__=="__main__":
	solution=Solution()
	print solution.longestCommonSubstring("AABCD", "ABCDA")