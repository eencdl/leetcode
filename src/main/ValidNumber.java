package main;

/**
 Validate if a given string is numeric.

 Some examples:
 "0" => true
 " 0.1 " => true
 "abc" => false
 "1 a" => false
 "2e10" => true
 Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.
 */
public class ValidNumber {
    public boolean isNumber(String s) {
        s = s.trim(); //Remove spaces

        String[] part = s.split("e");

        //Should be 1 (no e) or 2 (1 e)
        if(part.length == 0 || part.length > 2)
            return false;




       if(!valid(part[0],false))
           return false;

        //after e cannot have dot
       if(part.length == 2)
           if(!valid(part[1],true))
                return false;








        return true;


    }

    public boolean valid(String s,boolean hasDot) {

        //Get rid of prefixes
        if(s.length() > 0 && (s.charAt(0) == '+' || s.charAt(0) == '-'))
            s = s.substring(1);

        char[] c = s.toCharArray();

        if(c.length == 0 || s.equals("."))
            return false;


        for(int i=0; i<s.length(); i++) {
            if(c[i] == '.') {
                if(hasDot)
                    return false;

                hasDot = true;
            } else if (c[i] < '0' && c[i] > '9') {
                return false;
            }
        }
        return true;
    }
}
