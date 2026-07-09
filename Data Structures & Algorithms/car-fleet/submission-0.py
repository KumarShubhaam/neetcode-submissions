class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = {}
        for i,p in enumerate(position):
            pos_speed[p] = speed[i]

        # print('pos_speed', pos_speed)

        time = []
        position.sort()
        for p in position:
            s = pos_speed[p]
            t = (target - p)/s
            time.append(t)

        # print('time', time)
        min_t = time[-1]
        time_set = set()
        for t in range(len(time)-1, -1, -1):
            if time[t] <= min_t:
                time[t] = min_t
            else:
                min_t = time[t]
            time_set.add(time[t])
        
        # print('time after fleet', time)

        return len(time_set)
        