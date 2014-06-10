package main;



import java.util.List;

/**
 Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

 You may assume that the intervals were initially sorted according to their start times.

 Example 1:
 Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

 Example 2:
 Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

 This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
 */
public class InsertInterval {
    public List<Interval> insert(List<Interval> intervals, Interval newInterval) {
        int i = 0;
        while (i < intervals.size()) {
            Interval tmp = intervals.get(i);

            //No overlap, so we are done
            if (tmp.start > newInterval.end)
                break;


            if (tmp.start >= newInterval.start && tmp.end <= newInterval.end) {
                //old interval subset of new interval, take old out
                intervals.remove(i);
            } else if (tmp.start <= newInterval.start && tmp.end >= newInterval.end) {
                //newinterval subset of old interval, we are done
                return intervals;
            } else if (tmp.start <= newInterval.start && tmp.end >= newInterval.start) {
                //overlap front portion of new interval
                intervals.remove(i);
                newInterval.start = tmp.start;
            } else if (tmp.start >= newInterval.start && tmp.end >= newInterval.end) {
                //overlap back portion of new interval
                intervals.remove(i);
                newInterval.end = tmp.end;
            } else {
                i++; //consider next
            }

        }
        intervals.add(i, newInterval);
        return intervals;
    }
}
class Interval {
    int start;
    int end;
    Interval() { start = 0; end = 0; }
    Interval(int s, int e) { start = s; end = e; }
}