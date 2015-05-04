package main;

/**
 Write a function to find the longest common prefix string amongst an array of strings.
 */
public class LongestCommonPrefix {
    public String longestCommonPrefix(String[] strs) {

        if(strs.length == 0)
            return "";

        int j = 0;
        String tmp = strs[0];
        while(j < tmp.length()) {
            char c = tmp.charAt(j);
            for(int i=1; i<strs.length;i++) {
                if(j >= strs[i].length() || strs[i].charAt(j) != c){
                    return tmp.substring(0,j);
                }
            }
            j++;
        }
        return tmp.substring(0,j);
    }
}
