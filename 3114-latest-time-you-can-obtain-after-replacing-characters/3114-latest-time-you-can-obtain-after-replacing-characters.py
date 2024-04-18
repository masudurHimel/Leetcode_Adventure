class Solution:
    def findLatestTime(self, s: str) -> str:
        res = ''
        hour, minutes = s.split(":")
        
        if hour[0] == '?' and hour[1] == '?':
            res += '11'
        else:
            if hour[0] == '?' and hour[1] > '1':
                res += '0'
            elif hour[0] == '?':
                res += '1'
            else:
                res += hour[0]
            
            if hour[1] == '?' and hour[0] == '0':
                res += '9'
            elif hour[1] == '?' and hour[0] == '?':
                res += '9'
            elif hour[1] == '?':
                res += '1'
            else:
                res += hour[1]
            
        res += ':'
        
        if minutes[0] == '?':
            res += '5'
        else:
            res += minutes[0]
            
        if minutes[1] == '?':
            res += '9'
        else:
            res += minutes[1]
            
        return res
            
        