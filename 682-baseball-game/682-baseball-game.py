class Solution:
    def calPoints(self, ops: List[str]) -> int:
        record = []
        for i,v in enumerate(ops):
            if v == '+':
                record.append(int(record[-1]+record[-2]))
            elif v =='D':
                record.append(int(record[-1]*2))
            elif v == 'C':
                record = record[:-1]
            else:
                record.append(int(v))
                             
        return sum(record)