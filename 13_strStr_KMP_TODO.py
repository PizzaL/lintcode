import string

class Solution:
    def strStr(self, source, target):
    	if source is None or target is None :
    		return -1
        return source.find(target)

if __name__ == "__main__":
	solution=Solution()
	print solution.strStr("source", None)