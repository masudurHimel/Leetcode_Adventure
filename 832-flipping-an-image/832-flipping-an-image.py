class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in image:
            x,y = 0, len(i)-1
            while x <= y:
                i[x], i[y] = i[y]^1, i[x]^1
                x+=1
                y-=1
        return image