class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        num_fleets = 0
        cars = sorted(zip(position, speed), reverse = True)
        prev_time = 0
        for pos, spd in cars:
            time = (target - pos) / spd
            if time > prev_time:
                num_fleets += 1
                prev_time = time
        return num_fleets
