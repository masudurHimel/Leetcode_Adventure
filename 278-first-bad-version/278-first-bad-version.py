# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        s, l = 0, n
        flag = -1
        while s<=l:
            mid = (s+l)//2
            if isBadVersion(mid) == False:
                s = mid + 1
            else:
                flag = mid
                l = mid - 1
        return flag
                