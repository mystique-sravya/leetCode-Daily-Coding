class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        ns = ""
        for i in s:
            print(ord(i))
            if ord(i) in range(65, 91):
                ns += chr(ord(i)+32)
            else:
                ns += i
                
        return ns
        