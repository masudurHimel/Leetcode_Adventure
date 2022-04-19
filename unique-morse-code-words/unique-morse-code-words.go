func uniqueMorseRepresentations(words []string) int {
    morse_list := [26]string{".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."}
    
    char_list := make(map[string]string)
    
    for i:=0;i<26;i++{
        char_list[string(i+97)] = morse_list[i]
    }
    
    res_str := ""
    res_list := make(map[string]string)
    for i:=0;i<len(words);i++{
        res_str = ""
        for j:=0;j<len(words[i]);j++{
            res_str = res_str + char_list[string(words[i][j])]
        }
        res_list[res_str] = "abc"
    }
    
    return len(res_list)
}