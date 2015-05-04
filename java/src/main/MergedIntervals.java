package main;

import main.util.Interval;

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
class MyComparator implements Comparator {
    public int compare(Interval i1, Interval i2) {
        return i1.start - i2.start;
    }

    @Override
    public int compare(Object o1, Object o2) {
        Interval i1 = (Interval) o1;
        Interval i2 = (Interval) o2;
        return i1.start - i2.start;
    }
}


