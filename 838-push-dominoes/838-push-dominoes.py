class Solution:
    def pushDominoes(self, dominoes):
        dominoes = list(dominoes)
        start_flag = None
        end_flag = None
        start, end = 0, 0
        for i in range(len(dominoes)):
            if dominoes[i] == start_flag:
                diff = i - start - 1

                for j in range(start + 1, start + diff + 1):
                    dominoes[j] = start_flag

                start = i
                
                # continue

            if dominoes[i] == end_flag:
                end = i

                diff = end - start - 1

                if diff % 2 == 0:
                    for j in range(start+1, start + (diff//2)+1):
                        dominoes[j] = start_flag
                    for j in range(end - (diff//2), end):
                        dominoes[j] = end_flag
                else:
                    for j in range(start+1, start + (diff//2)+1):
                        dominoes[j] = start_flag
                    for j in range(end - (diff//2), end):
                        dominoes[j] = end_flag
                
                start, end = 0,0
                start_flag, end_flag = None, None
                
                # continue

            if dominoes[i] == 'L':
                start = i
                start_flag = 'L'
                # end_flag = 'R'
            if dominoes[i] == 'R':
                start = i
                start_flag = 'R'
                end_flag = 'L'

        for i in range(len(dominoes)):
            if dominoes[i] != '.':
                if dominoes[i] == 'L':
                    for j in range(i):
                        dominoes[j] = 'L'
                break


        for i in range(len(dominoes)-1, -1, -1):
            if dominoes[i] != '.':
                if dominoes[i] == 'R':
                    for j in range(len(dominoes)-1, i, -1):
                        dominoes[j] = 'R'
                break
                
        return ''.join(dominoes)