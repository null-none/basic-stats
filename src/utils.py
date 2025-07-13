class BasicStats:
    def __init__(self, numbers):
        self.numbers = numbers

    def mean(self):
        if not self.numbers:
            return None
        return sum(self.numbers) / len(self.numbers)

    def median(self):
        if not self.numbers:
            return None
        sorted_nums = sorted(self.numbers)
        n = len(sorted_nums)
        mid = n // 2
        if n % 2 == 1:
            return sorted_nums[mid]
        else:
            return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2

    def mode(self):
        if not self.numbers:
            return None
        freq = {}
        for num in self.numbers:
            freq[num] = freq.get(num, 0) + 1
        max_freq = max(freq.values())
        modes = [k for k, v in freq.items() if v == max_freq]
        if len(modes) == len(freq):
            return None
        return modes[0] if len(modes) == 1 else modes

    def min(self):
        if not self.numbers:
            return None
        return min(self.numbers)

    def max(self):
        if not self.numbers:
            return None
        return max(self.numbers)

    def rn(self):
        if not self.numbers:
            return None
        return self.max() - self.min()

    def variance(self):
        if not self.numbers or len(self.numbers) < 2:
            return None
        mean_val = self.mean()
        squared_diffs = [(x - mean_val) ** 2 for x in self.numbers]
        return sum(squared_diffs) / (len(self.numbers) - 1)

    def std_deviation(self):
        var = self.variance()
        if var is None:
            return None
        return var ** 0.5