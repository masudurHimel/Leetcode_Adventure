func shuffle(nums []int, n int) []int {
    res := make([]int, 0)
    for i:=0;i<len(nums)-n;i++{
        for j:=i;j<len(nums);j+=n{
            res = append(res, nums[j])
        }
    }
    return res
}