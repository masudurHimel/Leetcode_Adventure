func intersect(nums1 []int, nums2 []int) []int {
    res := make([]int, 0)
    target, sec := nums1, nums2
    
    if len(nums1) < len(nums2){
        target = nums1
        sec = nums2
    }else{
        target = nums2
        sec = nums1
    }
    for _,v := range target{
        for i,s := range sec{
            if v == s{
                sec[i] = -1
                res = append(res, v)
                break
            }
        }
    }
    return res
}