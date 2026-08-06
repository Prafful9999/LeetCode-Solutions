class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        

        ll = len(landStartTime)
        lw = len(waterStartTime)

        min_time = float('inf')

        # Land -> Water
        for i in range(ll):
            for j in range(lw):
                ltime = landStartTime[i] + landDuration[i]

                finish = max(ltime, waterStartTime[j]) + waterDuration[j]

                min_time = min(min_time, finish)

        # Water -> Land
        for i in range(lw):
            for j in range(ll):
                wtime = waterStartTime[i] + waterDuration[i]

                finish = max(wtime, landStartTime[j]) + landDuration[j]

                min_time = min(min_time, finish)

        return min_time
        