import csv
import time

from model import perforator
from manager import insertion_sort
from manager import heap_sort

if __name__ == '__main__':
    start_time = time.time()
    perforators_list = []
    with open('csv_list.csv', 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for line in csv_reader:
            perforators_list.append(perforator.Perforator(color=line[0], revolutions_per_minute=line[1],
                                                          stroke_frequency=line[2], producer_name=line[3]))
    print("Press any key for InsertionSort")
    input()
    insertion_sort = insertion_sort.InsertionSort()
    insertion_sort.sort_by_RPM_ascending(perforators_list, key=lambda perforator: perforator.revolutions_per_minute)
    print(perforators_list)
    print(insertion_sort)
    print(f"The program was executed in {time.time()-start_time} seconds")
    print("Press any key for HeapSort")
    input()
    start_time = time.time()
    heap_sort = heap_sort.HeapSort()
    heap_sort.sort(perforators_list, key=lambda perforator : perforator.stroke_frequency)
    print(perforators_list)
    print(heap_sort)
    print(f"The program was executed in {time.time()-start_time} seconds")
