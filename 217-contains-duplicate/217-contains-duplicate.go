func containsDuplicate(nums []int) bool {
    seen := make(map[int]bool)
    for i:=0;i<len(nums);i++{
        if _, exist := seen[nums[i]]; exist{
            return true
        }else{
            seen[nums[i]] = true
        }
    }
    return false
}