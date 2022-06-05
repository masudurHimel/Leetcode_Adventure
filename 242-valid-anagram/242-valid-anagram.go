func isAnagram(s string, t string) bool {
    if len(s)!=len(t){
        return false
    }
    
    resMap := make(map[byte]int)
    secMap := make(map[byte]int)
    var exist bool
    var secVal int
    
    for i:=0;i<len(s);i++{
        resMap[s[i]], exist = resMap[s[i]]
        
        if !exist{
            resMap[s[i]] = 1
        }else{
            resMap[s[i]]++
        }
    }
    
    for i:=0;i<len(t);i++{
        secMap[t[i]], exist = secMap[t[i]]
        
        if !exist{
            secMap[t[i]] = 1
        }else{
            secMap[t[i]]++
        }
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