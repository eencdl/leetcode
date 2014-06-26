package main;

/**
 Given an input string, reverse the string word by word.

 For example,
 Given s = "the sky is blue",
 return "blue is sky the".
 */
public class ReverseWordsInAString {

    public String reverseWords(String s) {
        s = s.trim(); //get rid of spaces
        if(s.length() == 0)
            return s;

        String result = "";
        int st = 0;
        int end = 0;
        while(end < s.length()) {

            if(s.charAt(st) != ' ') {
                if(s.charAt(end) == ' ' ) {
                    //only store if st != ' ' and end == ' '
                    result = s.substring(st,end) + " " + result;
                    st = end+1;
                }
            } else {
                //move st if is pointing to empty
                st++;
            }
            end++;
        }
        result = s.substring(st,end) + " " + result;

        return result.trim(); //in case of single word
    }
}
