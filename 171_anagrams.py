class Solution:
    # @param strs: A list of strings
    # @return: A list of strings
    def anagrams(self, strs):
        strMap={}
        for str in strs:
            newStr = ''.join(sorted(str))
            if newStr not in strMap:
                strMap[newStr]=[str]
            else:
                strMap[newStr].append(str)
        resList=[]
        for str, strList in strMap.items():
            if len(strList) > 1:
                resList += strList
        return resList

if __name__=="__main__":
	solution=Solution()
	print solution.anagrams(["lint", "intl", "inlt", "code"])