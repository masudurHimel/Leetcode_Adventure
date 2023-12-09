/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func inorderTraversal(root *TreeNode) []int {
    left, right := []int{}, []int{}
    if root == nil{
        return []int{}
    }else if root.Left != nil{
        left = inorderTraversal(root.Left)
    }
    
    left = append(left, root.Val)
    
    if root.Right != nil{
        right = inorderTraversal(root.Right)
    }
    
    return append(left, right...)
}