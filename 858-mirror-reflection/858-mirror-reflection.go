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
    l := lcm(p,q)
    x, y := (l / q) % 2, (l / p) % 2
    if x == 0{
        return 2
    }else if y == 1{
            return 1
    }else{
        return 0
    }
}