func search(nums []int, target int) int {
    l, h := 0, len(nums) -1
    var mid int
    for l<=h{
        mid = (l+h)/2
        if target == nums[mid]{
            return mid
        }else if target > nums[mid]{
            l = mid + 1 
        }else{
            h = mid - 1
        }
    }
    return -1
}