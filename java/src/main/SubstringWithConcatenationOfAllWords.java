package main;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

/**
 You are given a string, S, and a list of words, L, that are all of the same length. Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

 For example, given:
 S: "barfoothefoobarman"
 L: ["foo", "bar"]

 You should return the indices: [0,9].
 (order does not matter).
 */
public class SubstringWithConcatenationOfAllWords {
    //The idea is to have to have a hashmap doing the lookup
    public List<Integer> findSubstring(String S, String[] L) {
        List<Integer> result = new ArrayList<Integer>();
        HashMap<String,Integer> expected = new HashMap<String, Integer>();
        int m = L.length;
        int n = S.length();
        int l = L[0].length();
        //load all the substrings in expected first
        for(String str : L) {
            if(expected.containsKey(str)) {
                expected.put(str,expected.get(str)+1);
            } else {
                expected.put(str,1);
            }
        }

        for(int i=0; i<l; i++) {
            HashMap<String, Integer> actual = new HashMap<String, Integer>();
            int cnt = 0;
            int winLeft = i; //using sliding window concept

            for(int j=i; j<= n-l; j += l) {

                String current = S.substring(j, j + l);

                if (expected.containsKey(current)) {
                    //If found, increase counter
                    cnt++;
                    //Increment count in actual
                    if (actual.containsKey(current)) {
                        actual.put(current, actual.get(current) + 1);
                    } else {
                        actual.put(current, 1);
                    }

                    //We got more than
                    if (actual.get(current) > expected.get(current)) {

                        //extracting all the words until similar
                        //to current word
                        String tmp;
                        do {
                            tmp = S.substring(winLeft, winLeft + l);
                            actual.put(tmp, actual.get(tmp) - 1);
                            cnt--;
                            winLeft += l;
                        } while (!tmp.equals(current));
                    }

                    if (cnt == m) {
                        //add the result, we found first matching all substrings
                        result.add(winLeft);
                        //take out first word
                        String tmp = S.substring(winLeft,winLeft+l);
                        actual.put(tmp, actual.get(tmp) - 1);
                        cnt--;
                        winLeft += l;
                    }

                } else {
                    //Not found, reset
                    //and move window
                    actual.clear();
                    cnt = 0;
                    winLeft = j+l; //next word
                }
            }

        }
        return result;


    }
}
