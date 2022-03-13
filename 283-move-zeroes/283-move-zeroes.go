func moveZeroes(nums []int)  {
    count := 0
    i := 0
    for i<len(nums){
        if nums[i] == 0{
            count += 1
            nums = append(nums[:i], nums[i+1:]...)
        }else{
            i++
        }
    }
    temp := make([]int, count)
    nums = append(nums, temp...)
}