package main;

/**
 Given a roman numeral, convert it to an integer.

 Input is guaranteed to be within the range from 1 to 3999.
 */
public class RomanToInteger {
    /* If not familiar with roman numeral
     I - 1
     V - 5
     X - 10
     L - 50
     C - 100
     D - 500
     M - 1000
     I can be placed before V and X to make 4 units (IV) and 9 units (IX respectively)
     X can be placed before L and C to make 40 (XL) and 90 (XC respectively)
     C can be placed before D and M to make 400 (CD) and 900 (CM)
    */
    public int romanToInt(String s) {
        int sum = 0;
        int i=0;
        while(i < s.length()) {
            switch(s.charAt(i)) {
                case 'I':
                    //look ahead
                    if (i + 1 < s.length()) {
                        if (s.charAt(i + 1) == 'V') {
                            sum += 4;
                            i++;
                        } else if (s.charAt(i + 1) == 'X') {
                            sum += 9;
                            i++;
                        } else {
                            sum += 1;
                        }
                    } else {
                        sum += 1;
                    }
                    break;
                case 'V':
                    sum += 5;
                    break;
                case 'X':
                    //look ahead
                    if (i + 1 < s.length()) {
                        if (s.charAt(i + 1) == 'L') {
                            sum += 40;
                            i++;
                        } else if (s.charAt(i + 1) == 'C') {
                            sum += 90;
                            i++;
                        } else {
                            sum += 10;
                        }
                    } else {
                        sum += 10;
                    }
                    break;
                case 'L':
                    sum += 50;
                    break;
                case 'C':
                    //look ahead
                    if (i + 1 < s.length()) {
                        if (s.charAt(i + 1) == 'D') {
                            sum += 400;
                            i++;
                        } else if (s.charAt(i + 1) == 'M') {
                            sum += 900;
                            i++;
                        } else {
                            sum += 100;
                        }
                    } else {
                        sum += 100;
                    }
                    break;
                case 'D':
                    sum += 500;
                    break;
                case 'M':
                    sum += 1000;
                    break;
            }
            i++;
        }
        return sum;
    }
}
