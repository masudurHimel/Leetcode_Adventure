func reverseString(s []byte)  {
    len_s := len(s) - 1
    
    for i:=0;i<=len_s/2;i++{
        s[i], s[len_s-i] = s[len_s-i], s[i]
    }
    
}