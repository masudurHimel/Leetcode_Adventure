class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_list =[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse_dict = {}
        for i in range(len(morse_list)):
            morse_dict[chr(i+97)] = morse_list[i]
        
        res_set = set()
        for i in words:
            res_str = ""
            for j in i:
                res_str += morse_dict[j]
            res_set.add(res_str)
        return len(res_set)