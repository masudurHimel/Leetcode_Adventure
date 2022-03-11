/** 
 * Forward declaration of isBadVersion API.
 * @param   version   your guess about first bad version
 * @return 	 	      true if current version is bad 
 *			          false if current version is good
 * func isBadVersion(version int) bool;
 */

func firstBadVersion(n int) int {
    l, h := 0, n
    var mid int
    var flag int
    for l<=h{
        mid = (l+h)/2
        if isBadVersion(mid) == false{
            l = mid + 1
        }else{
            flag = mid
            h = mid - 1
        }
    }
    return flag
}