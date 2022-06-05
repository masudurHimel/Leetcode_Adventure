func isAnagram(s string, t string) bool {
    if len(s)!=len(t){
        return false
    }
    
    resMap := make(map[byte]int)
    secMap := make(map[byte]int)
    var exist bool
    var secVal int
    
    for i:=0;i<len(s);i++{
        resMap[s[i]] = 0
        resMap[t[i]] = 0
    }
    
    for i:=0;i<len(s);i++{
        resMap[s[i]]++
        secMap[t[i]]++
    }
     
    
    for k,v := range resMap{
        secVal, exist = secMap[k]
        
        if !exist{
            return false
        }
        
        if v != secVal{
            return false
        }
    }
    
    return true

}