func mergeAlternately(word1 string, word2 string) string {
    var min_len int
    if len(word1) < len(word2){
        min_len = len(word1)
    }else{
        min_len = len(word2)
    }
    
    res := ""
    i := 0
    for i=0;i<min_len;i++{
        res += word1[i:i+1] + word2[i:i+1]
    }
    
    
    if i < len(word1){
        res += word1[i:]
    }else if i < len(word2){
        res += word2[i:]
    }
    
    return res
}