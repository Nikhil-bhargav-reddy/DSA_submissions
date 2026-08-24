class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        

        task_start_time = customers[0][0]

        # idea is that we keep the inital task start time as the time when we begin first task
        # which equals first task start time
        # in cases where the start time of the current task is > assumed task start time, we re assign this to task start time

        for i in customers:
            if i[0] > task_start_time:
                i[1] = i[0] + i[1]
            else:
                i[1] = task_start_time + i[1]
            task_start_time =  i[1]

        print(customers)
        res = 0

        for j in customers:
            res =  res + j[1] - j[0]


        return res/len(customers)
        