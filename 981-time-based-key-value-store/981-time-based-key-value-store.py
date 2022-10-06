from sortedcontainers import SortedList
from bisect import bisect_left

class TimeMap:

    def __init__(self):
        self.d = dict()
        self.ts = SortedList()

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.ts.add(timestamp)
        self.d[f"{timestamp}-{key}"] = value
        

    def get(self, key: str, timestamp: int) -> str:
        ts = bisect_left(self.ts, timestamp)
        # print(self.d)
        # print(ts, timestamp, key)
        # print(self.ts)
        # print("--")
        if ts < len(self.ts) and self.ts[ts] == timestamp:
            i = 0
            while i <= len(self.ts):
                if res := self.d.get(f"{self.ts[ts-i]}-{key}"):
                    return res
                i += 1
            return ""
        
        else:
            if ts == 0:
                return ""
            i = 1
            while i <= len(self.ts):
                if res := self.d.get(f"{self.ts[ts-i]}-{key}"):
                    return res
                i += 1
            return ""
    

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)