func maxProfit(prices []int) int {
    min_v := 999999999999
    max_v := 0
    for _, i := range prices{
        if i < min_v{
            min_v = i
        }
        if (i - min_v) > max_v{
            max_v = i - min_v
        }
    }
    return max_v
}