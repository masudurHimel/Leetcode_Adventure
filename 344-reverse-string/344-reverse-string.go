func reverseString(s []byte)  {
    res := make([]byte, len(s))
    for i,j := len(s)-1, 0;i>=0;i,j = i-1,j+1{
        res[j] = s[i]
    }
    copy(s, res)
}