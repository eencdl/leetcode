package main;

import java.util.ArrayList;

/**
 The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

 P   A   H   N
 A P L S I I G
 Y   I   R
 And then read line by line: "PAHNAPLSIIGYIR"
 Write the code that will take a string and make this conversion given a number of rows:

 string convert(string text, int nRows);
 convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
 */
public class ZigZagConversion {
    public String convert(String s, int nRows) {
        if(s == null || s.length() <= 1 || nRows <= 1)
            return s;


        ArrayList<StringBuilder> tmp = new ArrayList<StringBuilder>();
        for(int i=0; i<nRows; i++) {
            tmp.add(new StringBuilder());
        }
        int i = 0;
        boolean down = true;
        int row = 0;
        while(i < s.length()) {
            tmp.get(row).append(s.charAt(i));
            if(row == 0) {
                down = true;
            } else if (row == nRows - 1) {
                down = false;
            }

            if(down)
                row++;
            else
                row--;

            i++;
        }
        String result = "";
        for(int j=0; j<nRows;j++) {
            result += tmp.get(j).toString();
        }
        return result;
    }
}
