class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in image:
            i[:] = i[::-1]
            i[:] = [0 if j==1 else 1 for j in i]
        
        return image