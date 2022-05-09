func checkIfPangram(sentence string) bool{
    res := make(map[rune]int)
    for _, ch := range sentence{
        res[ch] = 1
    }
    return len(res) == 26
}