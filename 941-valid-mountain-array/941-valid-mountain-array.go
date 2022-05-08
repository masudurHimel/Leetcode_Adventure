func validMountainArray(arr []int) bool {
    if len(arr) <= 2{
        return false
    }
    
    increasing, decreasing := false, false
    
    temp := arr[0]
    
    for i:=1;i<len(arr);i++{
        if arr[i] > temp && decreasing == false{
            increasing = true
        }else if arr[i] < temp && increasing == true{
            decreasing = true
        }else{
            return false
        }
        
        temp = arr[i]
    }
    
    if increasing == true && decreasing == true{
        return true
    }else{
        return false
    }
    
}




//         if len(arr) <= 2:
//             return False
        
//         increasing, decreasing = False, False
//         temp = arr[0]
//         for i in arr[1:]:
//             if i > temp and decreasing == False:
//                 increasing = True
//             elif i < temp and increasing == True:
//                 decreasing = True
            
//             else:
//                 return False
            
//             temp = i
          
//         if increasing and decreasing:
//             return True
//         return False
            