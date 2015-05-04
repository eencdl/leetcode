package main;

import java.util.Stack;

/**
 Evaluate the value of an arithmetic expression in Reverse Polish Notation.

 Valid operators are +, -, *, /. Each operand may be an integer or another expression.

 Some examples:
 ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
 ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
 */
public class EvaluateReversePolishNotation {
    //Just be careful of mixing negative number and operand
    //make sure the size of string is equal to one for operand
    public int evalRPN(String[] tokens) {

        String ops = "+-*/";
        Stack<String> stk = new Stack<String>();
        for(String s : tokens) {
            //make sure no empty strings
            if(s.length() > 0) {
                int opid = ops.indexOf(s);
                //cover the case of integer and negative values
                if (opid == -1 || s.length() > 1) {
                    stk.push(s);
                } else {
                    int tmp = 0;
                    //Notice the order, num1 is later than num2
                    int num2 = Integer.parseInt(stk.pop());
                    int num1 = Integer.parseInt(stk.pop());
                    switch (opid) {
                        case 0:
                            tmp = num1 + num2;
                            break;
                        case 1:
                            tmp = num1 - num2;
                            break;
                        case 2:
                            tmp = num1 * num2;
                            break;
                        case 3:
                            tmp = num1 / num2;
                            break;
                    }
                    stk.push(Integer.toString(tmp));
                }
            }
        }

        if(stk.empty())
            return 0;
        else
            return Integer.parseInt(stk.pop());

    }
}
