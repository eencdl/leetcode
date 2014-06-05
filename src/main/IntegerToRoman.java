package main;

/**
 Given an integer, convert it to a roman numeral.

 Input is guaranteed to be within the range from 1 to 3999.
 */
public class IntegerToRoman {
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
     public String intToRoman(int num) {
         String result = "";
         int tmp = num/1000; //get thousands
         while(tmp-- > 0)
             result += "M";

         num = num % 1000; //get hundreds
         tmp = num/100;

         if(tmp == 9) {
             result += "CM";
         } else if (tmp == 4) {
             result += "CD";
         } else {
             if(tmp >= 5) {
                 result += "D";
                 num = num % 500; //get remaining hundreds
             }
             tmp = num/100;
             while(tmp-- > 0)
                 result += "C";
         }

         num = num % 100; //get tens
         tmp = num/10;
         if(tmp == 9) {
             result += "XC";
         } else if (tmp == 4) {
             result += "XL";
         } else {
             if(tmp >= 5) {
                 result += "L";
                 num = num % 50; //get remaining tens
             }
             tmp = num/10;
             while(tmp-- > 0)
                 result += "X";
         }

         num = num % 10; //get ones
         if(num == 9) {
             result += "IX";
         } else if (num == 4) {
             result += "IV";
         } else {
             if(num >= 5) {
                 result += "V";
                 num = num % 5; //get remaining ones
             }
             while(num-- > 0)
                 result += "I";
         }

         return result;
     }
}
