class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Edge case: If `s` is empty, it's always a subsequence
        if not s:
            return True

        s_i = 0
        
        for i in t:
            # If the current character matches the character in `s`
            if s_i < len(s) and i == s[s_i]:
                s_i += 1
            # If all characters in `s` are matched, return True early
            if s_i == len(s):
                return True
        # If the loop finishes and not all of `s` is matched, return False
        return s_i == len
