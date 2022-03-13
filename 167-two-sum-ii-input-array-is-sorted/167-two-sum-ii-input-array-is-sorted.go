func twoSum(numbers []int, target int) []int {
    l := 0
    h := len(numbers) -1
    res := make([]int, 2)
    for l<h{
        if numbers[l] + numbers[h] > target{
            h = h-1
        }else if numbers[l] + numbers[h] < target{
            l = l+1
        }else{
            res[0], res[1] = l+1, h+1
            return res
        }
    }
    return res
}