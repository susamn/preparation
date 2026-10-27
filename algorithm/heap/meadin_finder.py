'''
295. Find Median from Data Stream
Hard
Topics
premium lock icon
Companies
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
 

Constraints:

-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.
 

Follow up:

If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
'''



'''
The trick is that you don't need the whole thing sorted — you only need to know the two elements straddling the middle.

Two heaps. Split the stream into a lower half and an upper half:

lo = max-heap holding the smaller half
hi = min-heap holding the larger half

Invariants: every element in lo ≤ every element in hi, and lo.size() == hi.size() or lo.size() == hi.size() + 1.

addNum: push onto one, then move the top across to restore balance. The cleanest version is the "push through" trick:

java
lo.offer(num);
hi.offer(lo.poll());
if (hi.size() > lo.size()) lo.offer(hi.poll());

Pushing into lo first then immediately moving its max to hi guarantees the ordering invariant without any comparison against the current median — you don't need an if (num < lo.peek()) branch. Then the size fixup.

findMedian: lo.size() > hi.size() ? lo.peek() : (lo.peek() + hi.peek()) / 2.0

O(log n) add, O(1) median.
'''

import heapq

class MedianFinder:
    def __init__(self):
        self.lo = []   # max-heap (negated), smaller half
        self.hi = []   # min-heap, larger half

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self) -> float:
        if len(self.lo) > len(self.hi):
            return float(-self.lo[0])
        return (-self.lo[0] + self.hi[0]) / 2.0


mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
print(mf.findMedian())    # 1.5

mf.addNum(3)
print(mf.findMedian())    # 2.0

neg = MedianFinder()
neg.addNum(-1)
print(neg.findMedian())   # -1.0
neg.addNum(-2)
print(neg.findMedian())   # -1.5
neg.addNum(-3)
print(neg.findMedian())   # -2.0
neg.addNum(-4)
print(neg.findMedian())   # -2.5