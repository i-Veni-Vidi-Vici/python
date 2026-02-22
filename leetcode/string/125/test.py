class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= s.lower()
        pal = ""

        for word in s:
            if word.isalnum():
                pal+=word
        a =list(pal)
        a.reverse()
        return pal == "".join(a)

# 3 ms

