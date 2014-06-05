package main;

import java.util.ArrayList;
import java.util.List;

/**
 Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

 You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

 Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

 For the last line of text, it should be left justified and no extra space is inserted between words.

 For example,
 words: ["This", "is", "an", "example", "of", "text", "justification."]
 L: 16.

 Return the formatted lines as:
 [
 "This    is    an",
 "example  of text",
 "justification.  "
 ]
 Note: Each word is guaranteed not to exceed L in length.
 */
public class TextJustification {
    public List<String> fullJustify(String[] words, int L) {
        List<String> results = new ArrayList<String>();
        ArrayList<String> buffer = new ArrayList<String>();
        String tmp  = "";
        int wordcnt = 0; // total word chars including space
        int avail  = 0;  // available for space
        int nsec   = 0;  // section of space needed
        int sps    = 0;  // space per section
        int remain = 0;  // remainder

        for(String word : words) {
            //check sentences including minimal 1 space between words
            if(wordcnt + word.length() + buffer.size() > L) {
                //Let's put 1 line into the final result
                nsec   =  buffer.size()-1;
                tmp = "";

                //If there is only 1 word
                if(nsec == 0) {
                    tmp += buffer.get(0);
                    //append spaces at the end
                    while(tmp.length() < L)
                        tmp += " ";
                } else {
                    //Multiple words, need to interleave
                    //spaces
                    avail  = L - wordcnt;
                    sps    =  avail/nsec;
                    remain =  avail % nsec;
                    for(int k=0; k < buffer.size(); k++) {
                        tmp += buffer.get(k);
                        //Adding spaces as follow
                        if(k < nsec) {
                            for(int x=0; x < sps; x++)
                                tmp += " ";

                            //spread the remaining
                            //spaces equally
                            if(remain-- > 0)
                                tmp += " ";
                        }
                    }
                }
                results.add(tmp);
                //reset
                wordcnt = 0;
                buffer = new ArrayList<String>();
            }
            buffer.add(word);
            wordcnt += word.length();
        }

        //Last line don't have to justify
        //but do have to fill up all the space
        // there are also cases where L is 0
        tmp = "";
        while(buffer.size() > 0) {
            tmp += buffer.get(0);
            buffer.remove(0);
            //Prevent adding unintened spaces
            //at the end
            if(buffer.size() != 0)
                tmp += " ";
        }
        while(tmp.length() < L)
            tmp += " ";

        results.add(tmp);
        return results;
    }
}
