from datetime import datetime


class HitCounter:
    def __init__(self):
        self.timestamp = [0] * 300
        self.count = [0] * 300

    def hit(self, timestamp):
        slot = timestamp % 300

        if self.timestamp[slot] == timestamp:
            self.count += 1
        else:
            self.timestamp[slot] = timestamp
            self.count = 1

    def getHit(self, timestamp):
        return sum([c for t, c in zip(self.timestamp, self.count) if timestamp - t <= 300])