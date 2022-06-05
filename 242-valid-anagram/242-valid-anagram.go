func isAnagram(s string, t string) bool {
    if len(s)!=len(t){
        return false
    }
    
    var resMap [26]int
    
    
    for i:=0;i<len(s);i++{
        resMap[s[i] - 'a']++
        resMap[t[i] - 'a']--
    }
     
    
    for _,v := range resMap{
        if v != 0{
            return false
        }
    }
    
    return true

}