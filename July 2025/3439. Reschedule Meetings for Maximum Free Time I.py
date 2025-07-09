class Solution(object):
    def maxFreeTime(self, eventTime, k, startTime, endTime):
        left_free_time = startTime[0] 
        right_free_time = startTime[k] - endTime[k-1] if k < len(startTime) else  eventTime - endTime[k-1]

        free_time_k = sum([startTime[i] - endTime[i-1] for i in range(1, k)]) + left_free_time + right_free_time
        ans = free_time_k

        for start_pos in range(1, max(1, len(startTime) - k)):
            free_time_k += (startTime[start_pos + k] - endTime[start_pos + k - 1]) - left_free_time
            left_free_time = startTime[start_pos] - endTime[start_pos - 1]

            ans = max(ans, free_time_k)
        if k != len(startTime):
            free_time_k += (eventTime - endTime[len(startTime) - 1]) - left_free_time
            ans = max(ans, free_time_k)

        return ans