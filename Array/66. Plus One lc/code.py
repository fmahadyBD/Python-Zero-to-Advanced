class Solution(object):
    def plusOne(self, d):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sum=0
        for i in range(0,len(d)):
            a=d[i]
            sum=sum*10+d[i]
        
        sum+=1
        arr = list(map(int, str(sum)))
        return arr