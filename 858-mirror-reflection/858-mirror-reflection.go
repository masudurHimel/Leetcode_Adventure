func lcm(a int, b int) int{
    var temp int
    c := a * b
    for b != 0 {
        temp = a % b
        a = b
        b = temp
    }
    return c/a
}
func mirrorReflection(p int, q int) int {
    x, y := (lcm(p,q) / q) % 2, (lcm(p,q) / p) % 2
    if x == 0{
        return 2
    }else{
        if y == 1{
            return 1
        }else{
            return 0
        }
    }
}