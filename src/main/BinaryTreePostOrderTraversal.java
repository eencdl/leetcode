package main;

import main.util.TreeNode;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

/**
 Given a binary tree, return the postorder traversal of its nodes' values.

 For example:
 Given binary tree {1,#,2,3},
 1
 \
 2
 /
 3
 return [3,2,1].

 Note: Recursive solution is trivial, could you do it iteratively?
 */
public class BinaryTreePostOrderTraversal {
    List<Integer> result = new ArrayList<Integer>();

    public List<Integer> postorderTraversal(TreeNode root) {
        if(root == null)
            return result;

        Stack<TreeNode> stk = new Stack<TreeNode>();
        stk.push(root);
        TreeNode prev = root;
        while(!stk.isEmpty()) {
            TreeNode tmp = stk.peek();
            //We pop the stack the current element either has no child
            //or it has the child of a previously pop element
            if( (tmp.left == null && tmp.right == null) ||
                (tmp.left == prev) ||
                (tmp.right == prev)) {
                result.add(tmp.val);
                stk.pop();
                prev = tmp;
            } else {
                if(tmp.right != null) stk.push(tmp.right);
                if(tmp.left != null) stk.push(tmp.left);
            }

        }
        return result;
    }
}
