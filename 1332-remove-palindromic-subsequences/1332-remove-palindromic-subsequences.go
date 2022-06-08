func removePalindromeSub(s string) int {
    p_s := ""
    for i:=len(s)-1;i>=0;i--{
        p_s += string(s[i])
    }
    
    if p_s == s{
        return 1
    }
    return 2
}