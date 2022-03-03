func nextGreaterElement(nums1 []int, nums2 []int) []int {
    var res []int
    flag := 0
    for i:=0;i<len(nums1);i++{
        flag = 0
        for j:=0;j<len(nums2);j++{
            if nums1[i] == nums2[j]{
                for z:=j+1;z<len(nums2);z++{
                    if nums2[z] > nums1[i]{
                        flag = 1
                        res = append(res, nums2[z])
                        break
                    }
                }
                
            }
        }
        if flag == 0{
                res = append(res, -1)
            }
    }
    return res
}