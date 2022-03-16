func kidsWithCandies(candies []int, extraCandies int) []bool {
    max_can := -999999999
    for _, i := range(candies){
        if i > max_can{
            max_can = i
        }
    }
    res := make([]bool, len(candies))
    var tmp int
    
    for ind,i := range candies{
        tmp = i + extraCandies
        if tmp >= max_can{
            res[ind] = true
        }else{
            res[ind] = false
        }
    }
    return res
}