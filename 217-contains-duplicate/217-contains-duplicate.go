func containsDuplicate(nums []int) bool {
    count := 1
    for i:=0;i<len(nums);i++{
        count = 1
        for j:=0;j<len(nums);j++{
            if i != j && nums[i] == nums[j]{
                count++
                return true
            }
        }
    }
    return false
}