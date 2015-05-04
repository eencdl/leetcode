package main;

/**
 Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

 For example,
 S = "ADOBECODEBANC"
 T = "ABC"
 Minimum window is "BANC".

 Note:
 If there is no such window in S that covers all characters in T, return the emtpy string "".

 If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
 */
public class MinimumWindowSubstring {
    //Idea here is to have 2 pointer, begin and end
    //First, try match the first window constraint
    //then we try to extend to the right
    //and then moving the begin to
    public String minWindow(String S, String T) {
        int slen = S.length();
        int tlen = T.length();
        int cnt = 0;
        int minlen = Integer.MAX_VALUE;
        int minBegin = 0;
        int minEnd = 0;

        int[] needToFind = new int[256]; //for all chars
        int[] hasFound   = new int[256];

        for(int i=0; i<tlen;i++){
            needToFind[T.charAt(i)]++;
        }

        int begin = 0;
        for(int end = 0; end < slen; end++) {

            //skip not match char
            if(needToFind[S.charAt(end)] == 0)
                continue;

            hasFound[S.charAt(end)]++;

            //We could have found more than what is need to find
            //We only count those need to find that is found
            //Not more than that
            if(hasFound[S.charAt(end)] <= needToFind[S.charAt(end)])
                cnt++;

            //the window constraint is satisfied
            if(cnt == tlen) {

                //Now move the begin pointer as far to the
                //right without breaking the window constraint
                while(hasFound[S.charAt(begin)] == 0 ||
                        hasFound[S.charAt(begin)] > needToFind[S.charAt(begin)] ){

                    if(hasFound[S.charAt(begin)] > needToFind[S.charAt(begin)])
                        hasFound[S.charAt(begin)]--;

                    begin++;
                }


                //store min begin, and len
                //if is minimum
                int len = end - begin + 1;
                if(minlen > len ) {
                    minlen = len;
                    minBegin = begin;
                    minEnd = end+1;
                }

            }



        }

        //remember java substring is beginIndex, endIndex
        //endIndex can be the length of the string
        //if beginIndex == endIndex, string = ""
        return S.substring(minBegin,minEnd);
    }

}
