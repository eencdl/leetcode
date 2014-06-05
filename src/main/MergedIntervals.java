package main;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

/**
 Given a collection of intervals, merge all overlapping intervals.

 For example,
 Given [1,3],[2,6],[8,10],[15,18],
 return [1,6],[8,10],[15,18].
 */
public class MergedIntervals {
    public List<Interval> merge(List<Interval> intervals) {
        List<Interval> result = new ArrayList<Interval>();
        if(intervals.size() == 0) return result;

        Collections.sort(intervals, new MyComparator());
        Interval prev = intervals.get(0);

        for(int i=1;i<intervals.size(); i++) {
            Interval current = intervals.get(i);
            //Remember it is <= NOT just <
            if(current.start <= prev.end) {
                prev.end = Math.max(prev.end,current.end);
            } else {
                result.add(prev);
                prev = current;
            }
        }
        result.add(prev);
        return result;
    }

}
class MyComparator implements Comparator<Interval> {
    public int compare(Interval i1, Interval i2) {
        return i1.start - i2.start;
    }
}
class Interval {
    int start;
    int end;
    Interval() { start = 0; end = 0; }
    Interval(int s, int e) { start = s; end = e; }
}

