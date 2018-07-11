def isPalindrome(s):
    result = True
    for i in range((len(s))//2):
        if s[i] != s[len(s)-i-1]:
            result = False
    return result

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        biggest = s[0]
        for i in range(len(s)-2):
            for j in range(i+2,len(s)+1):
                if isPalindrome(s[i:j]):
                    if len(s[i:j])>len(biggest):
                        biggest = s[i:j]
        return biggest
                        
s = Solution()
print(s.longestPalindrome('abcda'))
print(s.longestPalindrome('abcdamum'))
