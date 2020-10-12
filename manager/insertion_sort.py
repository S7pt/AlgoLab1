from manager.swap import swap


class InsertionSort:
    def __init__(self):
        self.swaps = 0
        self.comparisons = 0

    def sort_by_RPM_ascending(self, perforator_list, key=lambda object: object):
        for i in range(1, len(perforator_list)):
            j = i - 1
            buffer = key(perforator_list[i])
            while j >= 0 and key(perforator_list[j]) > buffer:
                self.comparisons += 2
                self.swaps += 1
                swap(perforator_list, j, j + 1)
                j -= 1

    def __repr__(self):
        return f"comparisons: {self.comparisons}, swaps: {self.swaps}"
