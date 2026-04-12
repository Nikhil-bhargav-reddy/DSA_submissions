"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        # multiple intervals
        # we need to check how many rooms we need to fit them all inside
        # 0 --------------------------40
        #     5-----10
        #                 15-----20
        # expected output is 2 rooms

        # when we see ifrst interval, we add one room
        # next interval comes in and we need to check the end time of previous interval to see if we can add incoming interval to same room
        # if not possible, we increment room count also keeping track of end times of intervals
        # 15 comes in and check which room is freeing up earliest? 2nd room it is, goes into second, incrments the second rooms max

        # we need to keep track of end times of meetings in a sorted order
        # if we could not find a place, we need to add a new room and add the end time to the sorted array and sort it again


        # min-heap is better to handle sorting this way?


        # setup a min heap to keep track of incoming end times, we just check if heap[0] is smaller than incoming start
        # if yes, we update out heap[0]'s end time to new end time-> wait we can do heapq.heappop(nums) and heap.heappush(new end time)

        # return len of heap at the end. 

        # Inpur should be sorted first though

        intervals_list = []

        for i in intervals:
            intervals_list.append([i.start, i.end])

        res = []

        heapq.heapify(res)

        intervals_list.sort(key=lambda i:i[0]) # sort by start time so that we have better way to organize in rooms

        for i in intervals_list:
            if res and res[0] <=i[0]: # if heap root min, is less or equal to incoming start time, we update
                    heapq.heappop(res) # pop smallest
                    heapq.heappush(res,i[1]) # push new intervals end time
            else: # if heap is empty or if incoming value is smaller than heap min end time
                heapq.heappush(res,i[1])
        return len(res)






        