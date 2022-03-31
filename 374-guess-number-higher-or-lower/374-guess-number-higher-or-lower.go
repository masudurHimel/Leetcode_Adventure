/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * func guess(num int) int;
 */

func guessNumber(n int) int {
    lo, hi := 1, n
    mid := 0
    tmp := 0
    for lo <=hi{
        mid = (lo+hi)/2
        tmp = guess(mid)
        if tmp == 0{
            return mid
        }else if tmp == 1{
            lo = mid +1
        }else{
            hi = mid -1
        }
    }
    return -1
}