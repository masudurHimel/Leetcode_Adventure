class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        temp_count = 0
        for i in grid:
            temp_count += i.count(0)
            
        x_axis = (len(grid)*len(grid)) - temp_count
        y_axis = []
        z_axis = []
        for i in grid:
            y_axis.append(max(i))
            
        t_matrix = [i for i in zip(*grid)]
        t_matrix = [i[::-1] for i in t_matrix]
        
        for i in t_matrix:
            z_axis.append(max(i))
        
        print(x_axis, y_axis, z_axis)
        # area calculation
        y_axis = sum(y_axis)
        z_axis = sum(z_axis)
        
        return x_axis+y_axis+z_axis
        
        
        