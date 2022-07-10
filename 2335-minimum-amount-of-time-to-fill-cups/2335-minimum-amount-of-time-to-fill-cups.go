func fillCups(amount []int) int {
    res := 0
    for amount[0] > 0 || amount[1] > 0 || amount[2] > 0{
        sort.Sort(sort.Reverse(sort.IntSlice(amount)))
        res++
        amount[0]--
        amount[1]--
    }
    return res
}