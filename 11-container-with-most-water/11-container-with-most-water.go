func maxArea(height []int) int {
    start := 0
    end := len(height) - 1
    max_area := 0
    var temp int

    for start <= end{
        if height[start] <= height[end]{
            temp = (end - start) * height[start]
            start += 1
        }else{
            temp = (end - start) * height[end]
            end -= 1
        }

        if temp > max_area{
            max_area = temp
        }
    }
    return max_area
}