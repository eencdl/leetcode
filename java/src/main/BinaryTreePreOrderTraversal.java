package main;

import main.util.TreeNode;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

/**
 Given a binary tree, return the preorder traversal of its nodes' values.

 For example:
 Given binary tree {1,#,2,3},
 1
 \
 2
 /
 3
 return [1,2,3].

 Note: Recursive solution is trivial, could you do it iteratively?
 */
public class BinaryTreePreOrderTraversal {
    //This is a DFS
    List<Integer> result = new ArrayList<Integer>();
    public List<Integer> preorderTraversal(TreeNode root) {
        if(root == null)
            return result;

        Stack<TreeNode> stk = new Stack<TreeNode>();
        stk.push(root);
        while(!stk.empty()) {
            TreeNode tmp = stk.pop();
            result.add(tmp.val);

            if(tmp.right != null) {
                stk.push(tmp.right);
            }

            if(tmp.left != null) {
                stk.push(tmp.left);
            }
        }
        return result;
    }
}
