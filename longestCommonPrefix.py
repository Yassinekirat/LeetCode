class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        short = min(strs, key=len)
        """for i in short:
            for string in strs:
                if string[i] != strs:"""
        