from config import settings


class Intervals:
    '''
    Represents the data vector as ascending and descending sequences. Information about the intervals can be accessed through the Intervals object.
    '''


    def __init__(self, vector):
        self.vector = [round(k, settings.ROUNDING) for k in vector]
        self.intervals = []
        self._find_extremes()

    def _find_extremes(self):
        start = 0
        end = 0

        for i in range(len(self.vector)):
            end = i

            if self._interval_end_point(i):
                difference = self.vector[end] - self.vector[start-1 if start > 0 else 0]
                self.intervals.append(Interval(difference, self.vector[start:end+1], start, end+1, len(self.vector)))
                start = i+1

    def _interval_end_point(self, i):
        v = self.vector
        if i == 0:
            return False
        if i == len(v) - 1:
            return True
        if v[i-1] < v[i] > v[i+1] or v[i-1] > v[i] < v[i+1]:
            return True
        if v[i-1] == v[i] > v[i+1] or v[i-1] == v[i] < v[i+1]:
            return True

        return False

    def total_length(self):
        return len([k for v in self.intervals for k in v ])

    def __getitem__(self, item):
        return self.intervals[item]

    def __len__(self):
        return len(self.intervals)

    def get_differences(self):
        return [iv.diff for iv in self.intervals]

    def get_lengths(self):
        return [len(iv) for iv in self.intervals]

    def get_intervals(self):
        return [iv.interval for iv in self.intervals]

    def __repr__(self):
        return str(self.intervals)



class Interval:
    '''
    A data object class for use with Intervals.
    '''

    def __init__(self, diff, interval, start, end, total_len):
        self.start, self.end = start, end
        self.diff = diff
        self.interval = interval
        self.total_len = total_len

    def relative_start(self):
        return self.start/self.total_len

    def relative_end(self):
        return self.end/self.total_len

    def __len__(self):
        return len(self.interval)

    def __getitem__(self, item):
        return self.interval[item]

    def __repr__(self):
        return str(self.interval)

