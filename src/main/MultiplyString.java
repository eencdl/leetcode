package main;

/**
 Given two numbers represented as strings, return multiplication of the numbers as a string.

 Note: The numbers can be arbitrarily large and are non-negative.
 */
public class MultiplyString {
    public String multiply(String num1, String num2) {
        char[] n1 = num1.toCharArray();
        char[] n2 = num2.toCharArray();
        int carry = 0;
        int i=num1.length()-1;
        int j=num2.length()-1;
        int len = i+j+2;
        int[] result = new int[len];
        for(int k=0;k<len;k++)
            result[k] = 0;

        for(; i>=0; i--){
            carry = 0;
            j=num2.length()-1;
            for(; j>=0; j--){
                int d1 = n1[i] - '0';
                int d2 = n2[j] - '0';
                int r = result[i+j+1];
                int mul = (d1*d2 + r + carry)%10;
                carry = (d1*d2 + r + carry)/10;
                result[i+j+1] =  mul;
            }
            result[i+j+1] = carry;
        }

        //convert to string
        String rs = "";
        boolean firstInt = false;
        for(int m=0;m<result.length;m++) {
            if(firstInt || result[m] != 0) {
                firstInt = true;
                rs = rs + result[m];
            }
        }
        //Make sure not empty
        if(rs.equals(""))
            rs = "0";

        return rs;
    }
}
