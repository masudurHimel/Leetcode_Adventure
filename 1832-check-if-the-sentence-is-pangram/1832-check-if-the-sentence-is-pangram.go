func checkIfPangram(sentence string) bool{
    res := make(map[string]int)
    for i:=0;i<len(sentence);i++{
        res[string(sentence[i])] = 1
    }
    return len(res) == 26
}