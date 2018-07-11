def isPalindrome(s):
    result = True
    for i in range((len(s))//2):
        if s[i] != s[len(s)-i-1]:
            result = False
    return result                          #returns Boolean to determine if is Palindrome

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:                    #return itself if it is either 1 character or empty (since it is technically a palindrome)
            return s
        biggest = s[0]                     #initiate biggest substring to first letter (longest palindrome can never be empty since 'a' is a palindrome)
        for i in range(len(s)-2):
            for j in range(i+2,len(s)+1):  #needs some work on the time complexity
                if isPalindrome(s[i:j]):   #conditional for every loop
                    if len(s[i:j])>len(biggest):
                        biggest = s[i:j]
        return biggest
                        
s = Solution()
print(s.longestPalindrome('abcda'))
print(s.longestPalindrome('abcdamum'))
