from manager.swap import swap

class HeapSort:
    def __init__(self):
        self.swaps=0
        self.comparisons=0

    def __repr__(self):
        return f"comparisons: {self.comparisons}, swaps: {self.swaps}"

    def heapify_reversed(self, perforator_list, heap_size, root_index, key=lambda obj: obj):
        least_element = root_index
        left_element = 2 * root_index + 1
        right_element = 2 * root_index + 2

        self.comparisons += 2
        if left_element < heap_size and key(perforator_list[least_element]) > key(perforator_list[left_element]):
            least_element = left_element

        self.comparisons += 2
        if right_element < heap_size and key(perforator_list[least_element]) > key(perforator_list[right_element]):
            least_element = right_element

        self.comparisons += 1
        if least_element != root_index:
            swap(perforator_list, root_index, least_element)
            self.swaps += 1
            HeapSort.heapify_reversed(self, perforator_list, heap_size, least_element, key)

    def sort(self, perforator_list, key=lambda obj: obj):
        heap_size = len(perforator_list)

        for i in range(heap_size // 2, -1, -1):
            HeapSort.heapify_reversed(self, perforator_list, heap_size, i, key)

        for i in range(heap_size - 1, 0, -1):
            swap(perforator_list, i, 0)
            self.swaps += 1
            HeapSort.heapify_reversed(self, perforator_list, i, 0, key)