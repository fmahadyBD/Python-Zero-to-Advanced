
# https://leetcode.com/problems/first-unique-character-in-a-string
# https://leetcode.com/problems/first-unique-character-in-a-string/
class Solution(object):
    def firstUniqChar(self, s):
        di = {}
        si = len(s)
        for i in range(si):
            key = s[i]
            if key not in di:
                di[key] = 1
            else:
                di[key] += 1

        for i in range(si):
            if di[s[i]] == 1:
                return i

        return -1
